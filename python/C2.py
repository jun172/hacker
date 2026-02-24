from scapy.all import sniff, IP
from collections import defaultdict
from datetime import datetime
import statistics

INTERVAL_VARIANCE = 1.0
MIN_COUNT = 6

timestamps = defaultdict(list)

def alert(src,dst):
    print(f"[ALERT] C2 Beacon suspected | src={src} -> dst={dst}")
    
def handler(pkt):
    if IP in pkt:
        src = pkt[IP].src
        dst = pkt[IP].dst
        now = datetime.now()
        
        key = (src,dst)
        timestamps[key].append(now)
        
        if len(timestamps[key]) >= MIN_COUNT:
            intervals = [
                (timestamps[key][i] - timestamps[key][i-1]).total_seconds()
                for i in range(1, len(timestamps[key]))
                ]
            if statistics.pvariance(intervals) < INTERVAL_VARIANCE:
                alert(src,dst)
                timestamps[key].clear()
print("[SOC] C2 beacon detector stared")
sniff(filter="ip", prn=handler, store=False)