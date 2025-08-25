from flask import Flask, request, jsonify
from services.anomaly import AnomalyDetector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # <-- Enable CORS for all routes

# Initialize detector
detector = AnomalyDetector()

# Health check
@app.route("/")
def home():
    return jsonify({"message": "Anomaly Detection Service is running!"})

# Train model endpoint
@app.route("/train", methods=["POST"])
def train():
    data = request.get_json()
    series = data.get("series", [])
    if not series:
        return jsonify({"error": "No data provided"}), 400

    detector.train(series)
    return jsonify({"status": "model trained", "samples": len(series)})

# Detect anomalies
@app.route("/detect", methods=["POST"])
def detect():
    data = request.get_json()
    point = data.get("point", [])
    if not point:
        return jsonify({"error": "No data point provided"}), 400

    try:
        result = detector.predict(point)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
