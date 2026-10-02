from contracts.tool_contract import ToolContract, ToolMetadata, ToolValidationError

def num(v,name,minimum=0):
    if isinstance(v,bool) or not isinstance(v,(int,float)) or v < minimum: raise ToolValidationError(f"{name} must be a number >= {minimum}")
    return float(v)

def nonempty(v,name):
    if not isinstance(v,str) or not v.strip(): raise ToolValidationError(f"{name} must be a non-empty string")
    return v.strip()
def validate(i):
    vehicles=i.get("vehicles");
    if not isinstance(vehicles,list) or not vehicles: raise ToolValidationError("vehicles must be a non-empty list")
    if len(vehicles)>10000: raise ToolValidationError("vehicles exceeds the safe batch limit")
    for v in vehicles:
        if not isinstance(v,dict) or not nonempty(v.get("vehicle_id"),"vehicle_id"): raise ToolValidationError("each vehicle requires vehicle_id")
        num(v.get("health_score"),"health_score"); num(v.get("fuel_l_per_100km"),"fuel_l_per_100km")

def execute(i):
    vs=i["vehicles"]; scores=[float(v["health_score"]) for v in vs]; fuel=[float(v["fuel_l_per_100km"]) for v in vs];
    return {"vehicle_count":len(vs),"average_health_score":round(sum(scores)/len(scores),2),"average_fuel_l_per_100km":round(sum(fuel)/len(fuel),2),"vehicles_requiring_attention":sum(s<60 for s in scores),"vehicles_on_watch":sum(60<=s<80 for s in scores)}

tool=ToolContract(ToolMetadata("summarize-fleet","Produce an aggregate fleet health and fuel summary from validated vehicle records.",{"type":"object"}),validate,execute)
