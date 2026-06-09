import logging
from typing import Tuple, List
from .types import TrafficData, AnomalyResult
from .exceptions import AnomalyDetectionError
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split

logger = logging.getLogger(__name__)

class AnomalyDetector:
    def __init__(self, contamination: float = 0.1):
        self.contamination = contamination
        self.model = IsolationForest(contamination=contamination)

    def train(self, traffic_data: List[TrafficData]) -> None:
        if not traffic_data:
            raise AnomalyDetectionError('Cannot train on empty data')
        X = np.array([td.features for td in traffic_data])
        y = np.array([td.label for td in traffic_data])
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train)

    def detect(self, traffic_data: TrafficData) -> AnomalyResult:
        try:
            features = np.array([traffic_data.features])
            prediction = self.model.predict(features)
            if prediction[0] == -1:
                return AnomalyResult(is_anomaly=True, confidence=self.model.decision_function(features)[0])
            else:
                return AnomalyResult(is_anomaly=False, confidence=self.model.decision_function(features)[0])
        except Exception as e:
            logger.error(f"Anomaly detection failed: {e}")
            raise AnomalyDetectionError("Failed to detect anomaly")

    def evaluate(self, traffic_data: List[TrafficData]) -> Tuple[float, float]:
        X = np.array([td.features for td in traffic_data])
        y = np.array([td.label for td in traffic_data])
        predictions = self.model.predict(X)
        precision = sum([1 for i in range(len(y)) if y[i] == 1 and predictions[i] == -1]) / sum([1 for i in range(len(y)) if predictions[i] == -1])
        recall = sum([1 for i in range(len(y)) if y[i] == 1 and predictions[i] == -1]) / sum([1 for i in range(len(y)) if y[i] == 1])
        return precision, recall