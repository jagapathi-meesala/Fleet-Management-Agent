---
name: fleet-monitoring
description: Assess vehicle operating health and identify fleet attention signals.
---
# Fleet Monitoring
## Purpose
Evaluate vehicle health using supplied operational indicators.
## Inputs
Vehicle identifier, odometer, engine hours, fault count, and service age.
## Processing
The agent validates types and applies deterministic penalties for faults, overdue service, and utilization anomalies.
## Outputs
A health score, status, and factor breakdown.
## Limitations
The score is an operational heuristic, not a mechanical diagnosis. Sensor quality and missing maintenance records can affect the result.
## Expected behavior
Reject malformed values and never invent missing measurements.
