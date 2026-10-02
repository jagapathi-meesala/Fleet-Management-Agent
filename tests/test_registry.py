import pytest
from core.agent_core import ToolRegistry
from tools import load_tools
def test_unknown_tool(): assert not load_tools(ToolRegistry()).execute("missing",{}).ok
def test_duplicate():
 reg=load_tools(ToolRegistry()); tool=reg.get("plan-maintenance")
 with pytest.raises(ValueError): reg.register(tool)
