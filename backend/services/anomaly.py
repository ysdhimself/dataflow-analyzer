import numpy as np
from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self):
        # Initialize Isolation Forest
        self.model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
        self.is_trained = False

    def train(self, data):
        """
        Train the anomaly detector.
        data: list of lists or numpy array
        """
        X = np.array(data)
        self.model.fit(X)
        self.is_trained = True

    def predict(self, data_point):
        """
        Predict if a point is anomaly.
        Returns: dict {is_anomaly, score}
        """
        if not self.is_trained:
            raise ValueError("Model not trained yet")

        X = np.array(data_point).reshape(1, -1)
        prediction = self.model.predict(X)[0]   # -1 = anomaly, 1 = normal
        score = self.model.decision_function(X)[0]

        return {
            "is_anomaly": bool(prediction == -1),   # <-- convert numpy.bool_ to Python bool
            "score": float(score)
        }
