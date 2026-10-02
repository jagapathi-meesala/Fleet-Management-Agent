from dataclasses import dataclass
from typing import Any, Callable, Mapping

class ToolValidationError(ValueError): pass

@dataclass(frozen=True)
class ToolMetadata:
    name: str
    description: str
    input_schema: Mapping[str, Any]

@dataclass
class ToolResult:
    ok: bool
    data: dict[str, Any] | None = None
    error: dict[str, str] | None = None

class ToolContract:
    def __init__(self, metadata: ToolMetadata, validator: Callable[[dict[str, Any]], None], executor: Callable[[dict[str, Any]], dict[str, Any]]):
        self.metadata=metadata; self._validator=validator; self._executor=executor
    def validate(self, inputs):
        if not isinstance(inputs, dict): raise ToolValidationError("Tool input must be an object")
        self._validator(inputs)
    def execute(self, inputs):
        self.validate(inputs)
        try: return ToolResult(True, self._executor(inputs), None)
        except (ValueError, TypeError, KeyError) as exc: return ToolResult(False, None, {"type": type(exc).__name__, "message": str(exc)})
