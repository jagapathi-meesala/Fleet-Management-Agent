# Rules

1. Reject missing, malformed, negative, or unsafe numeric inputs where the domain requires non-negative values.
2. Never fabricate telemetry, maintenance history, fuel use, or route data.
3. Keep calculations deterministic and explainable.
4. Do not expose environment secrets in outputs or logs.
5. Do not perform unsafe file operations or execute arbitrary commands from tool input.
6. Treat health scores as operational indicators, not mechanical diagnoses.
