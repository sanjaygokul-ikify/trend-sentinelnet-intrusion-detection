import unittest
from packages.core.anomaly_detector import AnomalyDetector
from packages.core.types import TrafficData, AnomalyResult

class TestAnomalyDetector(unittest.TestCase):
    def test_train(self):
        detector = AnomalyDetector()
        traffic_data = [TrafficData([1.0, 2.0, 3.0], 0)]
        detector.train(traffic_data)
        self.assertIsNotNone(detector.model)

    def test_detect(self):
        detector = AnomalyDetector()
        traffic_data = TrafficData([1.0, 2.0, 3.0], 0)
        result = detector.detect(traffic_data)
        self.assertIsInstance(result, AnomalyResult)

if __name__ == '__main__':
    unittest.main()