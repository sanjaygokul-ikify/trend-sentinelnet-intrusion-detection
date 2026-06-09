from typing import List, Dict
from dataclasses import dataclass

@dataclass
class TrafficData:
    features: List[float]
    label: int

@dataclass
class AnomalyResult:
    is_anomaly: bool
    confidence: float