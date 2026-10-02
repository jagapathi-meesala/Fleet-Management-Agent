from .portable_adapter import OpenAIAdapter, CrewAIAdapter, ClaudeCodeAdapter, LyzrAdapter

def build_adapter_registry():
    return {a.framework_name:a for a in (OpenAIAdapter(), CrewAIAdapter(), ClaudeCodeAdapter(), LyzrAdapter())}
