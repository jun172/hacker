import math
import re
from collections import defaultdict
from datetime import datetime, timedelta

WINDOW = 60

stats = defaultdict(lambda: {
    "queries": 0,
    "nxdomain": 0,
    "timestamps": [],
    "domains": []
})

def entropy(s):
    p = [s.count(c)/len(s) for c in set(s)]
    return -sum(x * math.log2(x) for x in p)

def is_base_encoded(domain):
    return re.match(r'^[a-zA-Z0-9+/=]+$', domain) is not None

def analyze(src_ip, domain, rcode):
    now = datetime.now()
    rec = stats[src_ip]

    rec["queries"] += 1
    rec["domains"].append(domain)
    rec["timestamps"].append(now)

    if rcode == 3:
        rec["nxdomain"] += 1

    # 時間窓制御
    rec["timestamps"] = [
        t for t in rec["timestamps"]
        if now - t < timedelta(seconds=WINDOW)
    ]

    score = 0

    if rec["nxdomain"] / (rec["queries"] + 1) > 0.4:
        score += 2

    if entropy(domain) > 3.8:
        score += 2

    if len(domain) > 40:
        score += 1

    if domain.count(".") > 5:
        score += 1

    if is_base_encoded(domain):
        score += 2

    if score >= 5:
        return {"type": "DNS_TUNNELING", "src": src_ip}

    return None
