---
name: maintenance-planning
description: Determine maintenance timing from mileage and service intervals.
---
# Maintenance Planning
## Purpose
Identify vehicles due or approaching scheduled service.
## Inputs
Vehicle identifier, odometer, days since service, and optional service intervals.
## Processing
Compare elapsed mileage/time against configured intervals and flag vehicles at or within the defined mileage threshold.
## Outputs
Due status, next service mileage, remaining days, and reason.
## Limitations
It does not diagnose component failure or replace manufacturer maintenance schedules.
## Expected behavior
Use supplied intervals when present and reject non-positive interval values.
