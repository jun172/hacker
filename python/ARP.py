import pyshark
import requests

INTERFACE = "en0" #macのWi-Fiは通常 en0
CAPTURE_TIME = 20 #秒

def lookup_vendor(mac):
    try:
        r = requests.get(
            f"https://api.macvendors.com/{mac}",
            timeout=5
        )
        return r.text if r.status_code == 200 else "Unkoown"
    except:
        return "Unkown"
    
print("[]")