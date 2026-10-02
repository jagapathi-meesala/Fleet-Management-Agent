from core.agent_core import ToolRegistry
from tools import load_tools
def r(): return load_tools(ToolRegistry())
def test_missing_required(): assert not r().execute("analyze-fuel-efficiency",{"distance_km":10,"fuel_litres":1}).ok
def test_negative_input(): assert not r().execute("analyze-fuel-efficiency",{"vehicle_id":"V1","distance_km":-1,"fuel_litres":1}).ok
def test_bad_batch(): assert not r().execute("summarize-fleet",{"vehicles":[]}).ok
