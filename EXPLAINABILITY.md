# Explainability

## Inputs and Data Sources
Inputs are supplied directly by an operator or an integrating system as structured JSON-like objects. Data used by the tools includes vehicle identifiers, odometer readings, engine hours, fault counts, service age, trip distance, fuel quantity, route distances, and fleet summary records; no external data source is silently queried.
The input mechanism is the framework-independent tool contract, which validates object shape and values before execution. Missing telemetry is rejected rather than inferred, and the tools do not create synthetic operational records.

## Decision and Reasoning
The decision process consists of validation followed by deterministic domain formulas. Fleet health subtracts bounded penalties for faults, service age, and utilization anomalies from a baseline score; maintenance planning compares elapsed service mileage/time with supplied or documented interval values; fuel and route tools use standard arithmetic ratios and deviations.
The agent decides which structured result to return from the selected tool and its validated inputs, while status thresholds are explicit in the implementation. The outputs expose the calculated factors or metrics so an operator can inspect why a status was produced.

## Limits and Constraints
The health score is an operational heuristic and is not a mechanical diagnosis, while maintenance planning does not replace manufacturer schedules or inspection procedures. Fuel and route metrics can be distorted by payload, terrain, weather, traffic, or inaccurate telemetry because those factors are outside the supplied calculation inputs.
The tools do not remotely control vehicles, execute repairs, or retrieve hidden fleet data. Malformed input, unsafe values, oversized batches, and missing required fields are rejected with structured errors.

## Input Requirements
All required fields must be present and use the expected types. Numeric measurements must be finite non-negative values unless a tool explicitly requires a positive denominator.

## Failure Handling
Validation failures return a structured error rather than a fabricated result. Execution errors are captured by the framework-independent contract and represented with an error type and message.

## Rules Applied
Tool calculations use explicit formulas and bounded penalties where applicable. No model-dependent judgment is required for the deterministic operational metrics.

## Constraints
Batch size is bounded by the tool's safe input limit, and runtime configuration is read from environment variables. Secrets are never embedded in source code or tool outputs.

## Expected Outputs
Successful calls return a structured object containing the vehicle identifier or fleet aggregate plus calculated metrics. Failed calls return `ok: false` with a structured error.

## Worked Example
For a vehicle with 8,000 km, 120 engine hours, two faults, and 45 days since service, the health calculation applies the documented penalties and returns a numeric score plus its factor breakdown. A maintenance call with a 10,000 km interval and 180-day interval then independently determines whether the vehicle is due or approaching service.

## Tool-by-Tool Explainability
### calculate-fleet-health
Inputs are vehicle_id, odometer_km, engine_hours, fault_count, and days_since_service. The tool computes explicit penalty components and returns health_score, status, and factor values.

### plan-maintenance
Inputs are vehicle_id, odometer_km, days_since_service, and optional service intervals. The tool computes remaining distance/time and marks maintenance due when an interval is reached or the vehicle is within the defined mileage threshold.

### analyze-fuel-efficiency
Inputs are vehicle_id, distance_km, and fuel_litres. The tool returns litres per 100 km and kilometres per litre using direct arithmetic.

### analyze-route-utilization
Inputs are vehicle_id, planned_distance_km, and actual_distance_km. The tool returns percentage deviation and a bounded utilization measure.

### summarize-fleet
Inputs are a non-empty list of validated vehicle records. The tool calculates average health, average fuel consumption, and counts vehicles requiring attention or watch status.
