from datetime import datetime
EVENTS = []

def add_event(event_type, src,dst=None, deteail=None,severity="HIGH"):
    EVENTS.append({
        "time":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type":event_type,
        "src":src,
        "dst":dst,
        "detail": deteail,
        "severity":severity
    })
    
def latest_events(limit=50):
    return EVENTS[-limit:]