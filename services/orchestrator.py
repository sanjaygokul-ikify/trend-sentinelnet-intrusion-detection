from packages.core.types import TrafficData, AnomalyResult
from packages.core.exceptions import AnomalyDetectionError
from packages.core.anomaly_detector import AnomalyDetector
import logging

logger = logging.getLogger(__name__)

class Orchestrator:
    def __init__(self):
        self.detector = AnomalyDetector()

    def train(self, traffic_data: list):
        self.detector.train(traffic_data)

    def detect(self, traffic_data: TrafficData) -> AnomalyResult:
        try:
            return self.detector.detect(traffic_data)
        except AnomalyDetectionError as e:
            logger.error(f"Anomaly detection failed: {e}")
            raise