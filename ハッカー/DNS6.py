import socket
import time
import math
from collections import defaultdict, Counter

# =====================
# Config
# =====================
DNS_PORT = 1054
WINDOW = 5          # seconds
ALERT_SCORE = 70

# =====================
# State
# =====================
window_start = time.time()
queries = []
nxdomain_count = 0

# =====================
# Utils
# =====================
def parse_domain(data):
    domain = ""
    idx = 12
    while idx < len(data):
        l = data[idx]
        if l == 0:
            break
        idx += 1
        domain += data[idx:idx+l].decode(errors="ignore") + "."
        idx += l
    return domain.rstrip(".")

def entropy(s):
    if not s:
        return 0
    freq = Counter(s)
    return -sum((c/len(s)) * math.log2(c/len(s)) for c in freq.values())

# =====================
# UDP Socket
# =====================
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", DNS_PORT))

print(f"[*] DNS IDS started on UDP {DNS_PORT}")

# =====================
# Main Loop
# =====================
while True:
    data, addr = sock.recvfrom(512)
    now = time.time()

    domain = parse_domain(data)
    ent = entropy(domain)

    # NXDOMAIN heuristic (ランダム系をNX扱い)
    is_nxdomain = ent > 3.2

    queries.append(domain)
    if is_nxdomain:
        nxdomain_count += 1

    print(f"[QUERY] {addr[0]} -> {domain} | ent={ent:.2f}")

    # =====================
    # Window Check
    # =====================
    if now - window_start >= WINDOW:
        total = len(queries)
        uniq = len(set(queries))
        nx_ratio = (nxdomain_count / total) if total else 0
        avg_entropy = sum(entropy(d) for d in queries) / total if total else 0

        # =====================
        # Score Aggregator
        # =====================
        score = 0
        score += min(total * 2, 30)               # Flood
        score += min(uniq * 3, 30)                # Brute force
        score += 30 if nx_ratio > 0.6 else 0      # NXDOMAIN
        score += 20 if avg_entropy > 3.2 else 0   # DGA

        print("\n[WINDOW]")
        print(f" total={total}")
        print(f" uniq={uniq}")
        print(f" nxdomain_ratio={nx_ratio:.2f}")
        print(f" avg_entropy={avg_entropy:.2f}")
        print(f" SCORE={score}")

        # =====================
        # ALERT
        # =====================
        if score >= ALERT_SCORE:
            print("🚨🚨🚨 ALERT: Distributed DNS Attack Detected 🚨🚨🚨")

        # Reset
        queries.clear()
        nxdomain_count = 0
        window_start = now
