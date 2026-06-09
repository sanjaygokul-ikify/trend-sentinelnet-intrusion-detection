import unittest
from services.orchestrator import Orchestrator
from packages.core.types import TrafficData, AnomalyResult

class TestPipeline(unittest.TestCase):
    def test_train_detect(self):
        orchestrator = Orchestrator()
        # Load training data
        traffic_data = [TrafficData([1.0, 2.0, 3.0], 0)]
        orchestrator.train(traffic_data)
        # Load test data
        test_data = TrafficData([4.0, 5.0, 6.0], 0)
        result = orchestrator.detect(test_data)
        self.assertIsInstance(result, AnomalyResult)

if __name__ == '__main__':
    unittest.main()