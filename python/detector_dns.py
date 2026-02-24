from scapy.all import sniff, DNS, DNSQR, IP
import math
from collections import defaultdict
from datetime import datetime, timedelta
from soc_core import add_event

MAX_LEN = 50
ENTROPY_THRESHOLD = 4.0
WINDOW = 60
COUNT_THRESHOLD = 5

cache = defaultdict(list)
def entropy(s):
    p = [s.count(c)/len(s) for c in set(s)]
    return -sum(x * math.log2(x) for x in p)
def handler(pkt):
    if IP in pkt and DNS in pkt and pkt[DNS].qr == 0:
        qname = pkt[DNSQR].qname.decode().strip(".")
        src = pkt[IP].src
        now = datetime.now()
        
        if len(qname) > MAX_LEN and entropy(qname) > ENTROPY_THRESHOLD:
            cache[src] = [t for t in cache[src] if now -t < timedelta(seconds=WINDOW)]
            cache[src].append(now)
            
            if len(cache[src]) >= COUNT_THRESHOLD:
                add_event(
                    event_type="DNS_TUNNELING",
                    src=src,
                    deteail=qname
                )
                cache[src].clear()

def start():
    sniff(filter="udp port 53", prn=handler, store=False)