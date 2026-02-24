from scapy.all import sniff, DNS, DNSQR, IP
import math
from collections import defaultdict
from datetime import datetime, timedelta

MAX_LEN = 50
ENTROPY_THRESHOLD = 4.0
WINDOW= 60
COUNT_THRESHOLD = 5

queries = defaultdict(list)

def entopy(s):
    prob = [s.count(c) / len(s) for c in set(s)]
    return -sum(p * math.log2(p) for p in prob)

def alert(ip, domain):
    print(f"[ALERT] DNS Tunneling suspected | src={ip} | domain={domain}")

def handler(pkt):
    if IP in pkt and DNS in pkt and pkt[DNS].qr == 0:
        qname = pkt[DNSQR].qname.decode().strip(".")
        src = pkt[IP].src
        now = datetime.now()
        
        e = entopy(qname)
        if len(qname) > MAX_LEN and e > ENTROPY_THRESHOLD:
            queries[src] = [t for t in queries[src] if now - t < timedelta(seconds=WINDOW)]
            queries[src].append(now)
            
            if len(queries[src]) >= COUNT_THRESHOLD:
                alert(src,qname)
                queries[src].clear()
                
print("[SOC] DNS tunneling detector started")
sniff(filter ="udp port 53", prn=handler, store=False)