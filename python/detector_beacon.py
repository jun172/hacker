from scapy.all import sniff, IP
from collections import defaultdict
from datetime import datetime
import statistics
from soc_core import add_event

INTERVAL_VARIANCE = 1.0
MIN_COUNT = 6

timestamps = defaultdict(list)

def handler(pkt):
    if IP in pkt:
        src = pkt[IP].src
        dst = pkt[IP].dst
        now = datetime.now()
        
        key = (src, dst)
        timestamps[key].append(now)
        
        if len(timestamps[key]) >= MIN_COUNT:
            intervals = [
                (timestamps[key][i] - timestamps[key][i-1]).total_seconds()
                for i in range(1, len(timestamps[key]))
            ]
            
            if statistics.pvariance(intervals) < INTERVAL_VARIANCE:
                add_event(
                    event_type="C2_BEACON",
                    src=src,
                    dst=dst,
                    deteail=f"intervals={intervals}"
                )
                timestamps[key].clear()
def start():
    sniff(filter="ip", prn=handler,store=False)