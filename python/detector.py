import random
import time

SUSPICIOUS_EVENTS = [
    "SSH brute force detected",
    "Unauthorized API access",
    "Suspicious IP behavior",
    "Port scan detected"
]

def analyze_log():
    """
    疑似ログ解析
    本物SOCなら:
    - auth.log
    - nginx access.log
    - audit.log
    """
    time.sleep(3)
    
    if random.randint(1,5) == 3:
        return {
            "event": random.choice(SUSPICIOUS_EVENTS),
            "severity": "HIGH",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
    return None