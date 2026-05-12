import requests
import time

URL="http://127.0.0.1:5000"
DELAY = 0.2

session = requests.Session()

try:
    while True:
        r = session.get(URL, timeout=3)
        print("[OK]",r.status_code)
        time.sleep(DELAY)
except KeyboardInterrupt:
    print("\n[!] Stopped by user")
finally:
    session.close()