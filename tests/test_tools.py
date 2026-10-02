from core.agent_core import ToolRegistry
from tools import load_tools
def r(): return load_tools(ToolRegistry())
def test_health(): assert r().execute("calculate-fleet-health",{"vehicle_id":"V1","odometer_km":8000,"engine_hours":120,"fault_count":0,"days_since_service":10}).data["status"]=="healthy"
def test_maintenance(): assert r().execute("plan-maintenance",{"vehicle_id":"V1","odometer_km":19500,"days_since_service":20}).data["maintenance_due"]
def test_route(): assert r().execute("analyze-route-utilization",{"vehicle_id":"V1","planned_distance_km":100,"actual_distance_km":105}).data["status"]=="efficient"
def test_summary(): assert r().execute("summarize-fleet",{"vehicles":[{"vehicle_id":"V1","health_score":90,"fuel_l_per_100km":8}]}).data["vehicle_count"]==1
