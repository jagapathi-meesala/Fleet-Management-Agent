from contracts.tool_contract import ToolContract, ToolMetadata, ToolValidationError

def num(v,name,minimum=0):
    if isinstance(v,bool) or not isinstance(v,(int,float)) or v < minimum: raise ToolValidationError(f"{name} must be a number >= {minimum}")
    return float(v)

def nonempty(v,name):
    if not isinstance(v,str) or not v.strip(): raise ToolValidationError(f"{name} must be a non-empty string")
    return v.strip()
def validate(i):
    nonempty(i.get("vehicle_id"),"vehicle_id"); num(i.get("odometer_km"),"odometer_km"); num(i.get("days_since_service"),"days_since_service")
    if "service_interval_km" in i: num(i["service_interval_km"],"service_interval_km",1)
    if "service_interval_days" in i: num(i["service_interval_days"],"service_interval_days",1)

def execute(i):
    km=num(i["odometer_km"],"odometer_km"); days=num(i["days_since_service"],"days_since_service"); ikm=num(i.get("service_interval_km",10000),"service_interval_km",1); idays=num(i.get("service_interval_days",180),"service_interval_days",1)
    km_left=ikm-(km%ikm); days_left=idays-days
    due=days_left<=0 or km_left<=500
    return {"vehicle_id":i["vehicle_id"],"maintenance_due":due,"next_service_km":km+max(0,km_left),"days_until_service":max(0,days_left),"reason":"service interval reached or within 500 km" if due else "within configured service interval"}

tool=ToolContract(ToolMetadata("plan-maintenance","Determine whether a vehicle is due or approaching scheduled maintenance.",{"type":"object"}),validate,execute)
