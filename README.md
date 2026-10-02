# Fleet Management Agent

A framework-independent fleet operations agent implementing transparent vehicle health, maintenance planning, fuel-efficiency, route-utilization, and fleet-summary tools.

## Architecture
`FleetAgent` delegates to a dynamic `ToolRegistry`; every tool implements `ToolContract`; adapters expose the same core to OpenAI SDK, CrewAI, Claude Code, and Lyzr-shaped integration points without importing those frameworks.

## Installation
Use Python 3.10+ and install `requirements.txt` in an isolated environment.

## Configuration
Runtime configuration is supplied through `FLEET_ENVIRONMENT`, `FLEET_LOG_LEVEL`, `FLEET_MAX_BATCH_SIZE`, and `FLEET_MAINTENANCE_DUE_DAYS`. No secrets or runtime values are committed.

## Tools
- calculate-fleet-health
- plan-maintenance
- analyze-fuel-efficiency
- analyze-route-utilization
- summarize-fleet

## Skills
- fleet-monitoring
- maintenance-planning
- fleet-analytics

## Usage
Import the registry and register tools from `tools.load_tools`, then call `FleetAgent.run(tool_name, inputs)`.

## Testing
Run `pytest -q`. The suite covers core execution, tools, contracts, registry, adapters, documentation, security, invalid inputs, and manifest validation.

## Portability
The core does not depend on OpenAI, CrewAI, Claude, or Lyzr SDKs. Adapter classes provide a stable integration boundary; this repository does not claim vendor runtime certification without external integration tests.

## Limitations
Results depend on the quality and completeness of supplied telemetry. The health score is a heuristic and should not replace professional inspection or manufacturer guidance.
