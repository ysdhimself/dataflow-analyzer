# models/ml_model.py
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib
import os

MODEL_FILE = "models/anomaly_model.pkl"

class AnomalyModel:
    def __init__(self):
        self.model = None
        self.is_trained = False
        if os.path.exists(MODEL_FILE):
            self.load_model()

    def train(self, data):
        X = np.array(data)
        # Using IsolationForest for simplicity; can replace with TF/PyTorch model later
        self.model = IsolationForest(contamination=0.1, random_state=42)
        self.model.fit(X)
        self.is_trained = True
        self.save_model()
        return {"samples": len(data), "status": "model trained"}

    def detect(self, point):
        if not self.is_trained:
            return {"error": "Model not trained yet"}
        X_point = np.array([point])
        score = self.model.decision_function(X_point)[0]
        is_anomaly = self.model.predict(X_point)[0] == -1
        return {"is_anomaly": bool(is_anomaly), "score": float(score)}

    def save_model(self):
        os.makedirs("models", exist_ok=True)
        joblib.dump(self.model, MODEL_FILE)

    def load_model(self):
        self.model = joblib.load(MODEL_FILE)
        self.is_trained = True
