# Architecture RFC

## System Design
SentinelNet employs a distributed sensor network (3+ replicas) communicating with centralized analysis nodes. Each sensor implements:
- Local anomaly detection
- Event encryption
- Autonomous containment

## Data Flow
1. Sensors collect traffic patterns
2. Anomalies are classified using ML
3. Confirmed threats trigger containment
4. Patterns are aggregated for global analysis

## Scaling
Horizontal scaling achieved via global load balancing with automatic service node spawning in K8s clusters. Uses CRDTs for consistent state management across distributed nodes.