from core.agent_core import FleetAgent, ToolRegistry
from tools import load_tools
def agent(): return FleetAgent(load_tools(ToolRegistry()))
def test_discovery(): assert len(agent().tools())==5
def test_execution():
 r=agent().run("analyze-fuel-efficiency",{"vehicle_id":"V1","distance_km":200,"fuel_litres":20}); assert r.ok and r.data["litres_per_100km"]==10
