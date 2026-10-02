from pathlib import Path
from contracts.tool_contract import ToolResult, ToolValidationError

class ToolRegistry:
    def __init__(self): self._tools={}
    def register(self, tool):
        name=tool.metadata.name
        if name in self._tools: raise ValueError(f"Tool already registered: {name}")
        self._tools[name]=tool
    def discover(self): return sorted(self._tools)
    def get(self,name):
        if name not in self._tools: raise KeyError(f"Unknown tool: {name}")
        return self._tools[name]
    def execute(self,name,inputs):
        try: return self.get(name).execute(inputs)
        except KeyError as exc: return ToolResult(False,error={"type":"UnknownTool","message":str(exc)})
        except ToolValidationError as exc: return ToolResult(False,error={"type":"ValidationError","message":str(exc)})

class FleetAgent:
    def __init__(self, registry): self.registry=registry
    def tools(self): return self.registry.discover()
    def run(self, tool_name, inputs): return self.registry.execute(tool_name, inputs)
