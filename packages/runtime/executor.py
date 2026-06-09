import logging
from typing import List
from ..core.engine import AnomalyDetector
from ..core.types import TrafficData, AnomalyResult
from ..core.exceptions import AnomalyDetectionError

logger = logging.getLogger(__name__)

class Executor:
    def __init__(self, detector: AnomalyDetector):
        self.detector = detector

    def execute(self, traffic_data: List[TrafficData]) -> List[AnomalyResult]:
        results = []
        for data in traffic_data:
            try:
                result = self.detector.detect(data)
                results.append(result)
            except AnomalyDetectionError as e:
                logger.error(f"Failed to detect anomaly: {e}")
                results.append(AnomalyResult(is_anomaly=False, confidence=0))
        return results