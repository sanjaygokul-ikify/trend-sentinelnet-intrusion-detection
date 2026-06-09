import argparse
from services.orchestrator import Orchestrator
from packages.core.types import TrafficData
import logging

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='Anomaly Detection CLI')
parser.add_argument('--train', action='store_true', help='Train the model')
parser.add_argument('--detect', action='store_true', help='Detect anomalies')
args = parser.parse_args()

orchestrator = Orchestrator()

if args.train:
    # Load training data
    traffic_data = [TrafficData([1.0, 2.0, 3.0], 0)]
    orchestrator.train(traffic_data)

if args.detect:
    # Load test data
    traffic_data = TrafficData([4.0, 5.0, 6.0], 0)
    result = orchestrator.detect(traffic_data)
    logger.info(f"Detected anomaly: {result.is_anomaly}, confidence: {result.confidence}")