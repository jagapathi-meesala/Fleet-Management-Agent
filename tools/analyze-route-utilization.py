from contracts.tool_contract import ToolContract, ToolMetadata, ToolValidationError

def num(v,name,minimum=0):
    if isinstance(v,bool) or not isinstance(v,(int,float)) or v < minimum: raise ToolValidationError(f"{name} must be a number >= {minimum}")
    return float(v)

def nonempty(v,name):
    if not isinstance(v,str) or not v.strip(): raise ToolValidationError(f"{name} must be a non-empty string")
    return v.strip()
def validate(i):
    nonempty(i.get("vehicle_id"),"vehicle_id"); num(i.get("planned_distance_km"),"planned_distance_km",0.01); num(i.get("actual_distance_km"),"actual_distance_km",0.0)

def execute(i):
    p=num(i["planned_distance_km"],"planned_distance_km",0.01); a=num(i["actual_distance_km"],"actual_distance_km",0); deviation=round((a-p)/p*100,2); utilization=round(min(100,p/a*100) if a else 0,2)
    return {"vehicle_id":i["vehicle_id"],"planned_distance_km":p,"actual_distance_km":a,"distance_deviation_percent":deviation,"route_utilization_percent":utilization,"status":"efficient" if abs(deviation)<=10 else "review"}

tool=ToolContract(ToolMetadata("analyze-route-utilization","Measure route deviation and utilization against a planned trip distance.",{"type":"object"}),validate,execute)
