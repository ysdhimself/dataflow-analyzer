from flask import Flask, request, jsonify
from flask_cors import CORS
from services.anomaly import train_anomalies, detect_anomaly

app = Flask(__name__)
CORS(app)  # allow frontend to communicate

@app.route('/train', methods=['POST'])
def train():
    data = request.get_json()
    series = data.get("series")
    if not series:
        return jsonify({"error": "No series provided"}), 400
    result = train_anomalies(series)
    return jsonify(result)

@app.route('/detect', methods=['POST'])
def detect():
    data = request.get_json()
    point = data.get("point")
    if not point:
        return jsonify({"error": "No point provided"}), 400
    result = detect_anomaly(point)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
