from contracts.tool_contract import ToolContract, ToolMetadata, ToolValidationError

def num(v,name,minimum=0):
    if isinstance(v,bool) or not isinstance(v,(int,float)) or v < minimum: raise ToolValidationError(f"{name} must be a number >= {minimum}")
    return float(v)

def nonempty(v,name):
    if not isinstance(v,str) or not v.strip(): raise ToolValidationError(f"{name} must be a non-empty string")
    return v.strip()
def validate(i):
    num(i.get("distance_km"),"distance_km",0.01); num(i.get("fuel_litres"),"fuel_litres",0.01); nonempty(i.get("vehicle_id"),"vehicle_id")

def execute(i):
    d=num(i["distance_km"],"distance_km",0.01); f=num(i["fuel_litres"],"fuel_litres",0.01); lpk=round(f/d*100,2); kpl=round(d/f,2)
    return {"vehicle_id":i["vehicle_id"],"distance_km":d,"fuel_litres":f,"litres_per_100km":lpk,"km_per_litre":kpl}

tool=ToolContract(ToolMetadata("analyze-fuel-efficiency","Compute standard fuel-efficiency metrics for a vehicle trip.",{"type":"object"}),validate,execute)
