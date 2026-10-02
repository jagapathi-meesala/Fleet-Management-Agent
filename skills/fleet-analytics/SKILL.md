---
name: fleet-analytics
description: Analyze fuel efficiency, route utilization, and fleet aggregates.
---
# Fleet Analytics
## Purpose
Compute transparent operational metrics for fleet reporting.
## Inputs
Trip distance, fuel use, planned and actual route distance, or validated vehicle summaries.
## Processing
Use standard arithmetic metrics with explicit denominators and bounded inputs.
## Outputs
Fuel consumption, route deviation, utilization, and aggregate fleet indicators.
## Limitations
The analytics do not account for terrain, payload, weather, traffic, or vehicle-specific manufacturer baselines unless those factors are supplied separately.
## Expected behavior
Return structured numeric results and reject invalid or empty batches.
