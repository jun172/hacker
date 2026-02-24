import math
from collections import defaultdict
from datetime import datetime, timedelta

WINDOW = 60
NX_THRESHOLD = 5
ENTROPY_THRESHOLD = 3.8

stats = defaultdict(lambda:{
    "nxdomain":0,
    "queries":0,
    "timestamps":[]
})

def entropy(s):
    p = [s.count(c)/len(s) for c in set(s)]
    return -sum(x * math.log2(x) for x in p)

def process_dns(src_ip, domain, rcode):
    now = datetime.now()
    record = stats[src_ip]
    
    record["queries"] += 1
    record["timesstamps"].append(now)
    
    # NXDOMAIN判定
    if rcode == 3:
        record["nxdomain"] += 1
    
    #古いデータ削除
    record["timesstamps"] = [
        t for t in record["timestamps"]
        if now - t < timedelta(seconds=WINDOW)
    ]
    
    score = 0
    
    if record["nxdomain"] >= NX_THRESHOLD:
        score += 2
        
    if entropy(domain) > ENTROPY_THRESHOLD:
        score += 2
    
    if len(domain) > 40:
        score += 1
        
    if score >= 4:
        return {
            "type":"DNS_ANOMALY",
            "src": src_ip,
            "domain":domain,
            "score":score
        }
        
    return None