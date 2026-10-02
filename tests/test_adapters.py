from adapters import build_adapter_registry
def test_adapters():
 a=build_adapter_registry(); assert set(a)=={"OpenAI SDK","CrewAI","Claude Code","Lyzr"}
