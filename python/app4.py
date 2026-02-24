from fastapi import FastAPI
import threading
from soc_core import latest_events
import detector_dns
import detector_beacon

app = FastAPI(title="Mini SIEM SOC")

@app.on_event("startup")
def start_detectors():
    threading.Thread(target=detector_dns.start, daemon=True).start()
    threading.Thread(target=detector_beacon.start, daemon=True).start()
    
@app.get("/enents")
def events():
    return latest_events()

@app.get("/")
def dashboard():
    return {
        "status": "SOC runing",
        "event_count":len(latest_events())
    }