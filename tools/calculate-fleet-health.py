from contracts.tool_contract import ToolContract, ToolMetadata, ToolValidationError

def num(v,name,minimum=0):
    if isinstance(v,bool) or not isinstance(v,(int,float)) or v < minimum: raise ToolValidationError(f"{name} must be a number >= {minimum}")
    return float(v)

def nonempty(v,name):
    if not isinstance(v,str) or not v.strip(): raise ToolValidationError(f"{name} must be a non-empty string")
    return v.strip()
def validate(i):
    for k in ("vehicle_id","odometer_km","engine_hours","fault_count","days_since_service"): pass
    nonempty(i.get("vehicle_id"),"vehicle_id"); num(i.get("odometer_km"),"odometer_km"); num(i.get("engine_hours"),"engine_hours"); num(i.get("fault_count"),"fault_count"); num(i.get("days_since_service"),"days_since_service")

def execute(i):
    km=num(i["odometer_km"],"odometer_km"); hours=num(i["engine_hours"],"engine_hours"); faults=num(i["fault_count"],"fault_count"); days=num(i["days_since_service"],"days_since_service")
    fault_penalty=min(40,faults*8); service_penalty=min(30,max(0,(days-30)*0.5)); utilization_penalty=0 if hours==0 else min(20,max(0,(km/(hours+1))-70)*0.2)
    score=round(max(0,100-fault_penalty-service_penalty-utilization_penalty),2)
    status="healthy" if score>=80 else "watch" if score>=60 else "attention_required"
    return {"vehicle_id":i["vehicle_id"],"health_score":score,"status":status,"factors":{"fault_penalty":round(fault_penalty,2),"service_penalty":round(service_penalty,2),"utilization_penalty":round(utilization_penalty,2)}}

tool=ToolContract(ToolMetadata("calculate-fleet-health","Calculate a deterministic vehicle health score from operational indicators.",{"type":"object"}),validate,execute)
