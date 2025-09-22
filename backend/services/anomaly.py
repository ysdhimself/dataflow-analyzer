# services/anomaly.py
from models.ml_model import AnomalyModel

anomaly_service = AnomalyModel()

def train_anomalies(data):
    return anomaly_service.train(data)

def detect_anomaly(point):
    return anomaly_service.detect(point)
