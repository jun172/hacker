import socket, time, struct, math
from collections import defaultdict, deque

DNS_PORT = 1054
WINDOW = 10

stats = defaultdict(lambda: deque())

def entropy(s):
    from collections import Counter
    c = Counter(s)
    return -sum((v/len(s)) * math.log2(v/len(s)) for v in c.values())

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", DNS_PORT))

print("[*] DNS5 IDS started on UDP", DNS_PORT)

while True:
    data, addr = sock.recvfrom(512)
    now = time.time()
    src_ip, src_port = addr

    # --- Domain parse ---
    idx = 12
    domain = ""
    while data[idx] != 0:
        l = data[idx]
        idx += 1
        domain += data[idx:idx+l].decode(errors="ignore") + "."
        idx += l
    domain = domain[:-1]

    sub = domain.split(".")[0]
    ent = entropy(sub)

    stats[src_ip].append({
        "t": now,
        "domain": domain,
        "entropy": ent
    })

    # window cleanup
    stats[src_ip] = deque(
        [x for x in stats[src_ip] if now - x["t"] < WINDOW]
    )

    uniq = len(set(x["domain"] for x in stats[src_ip]))
    avg_entropy = sum(x["entropy"] for x in stats[src_ip]) / len(stats[src_ip])

    print(f"[DNS5] {src_ip}:{src_port}")
    print(f"  domain={domain}")
    print(f"  uniq={uniq} avg_entropy={avg_entropy:.2f}")

    if uniq > 20 and avg_entropy > 3.0:
        print("🚨 DNS5 ALERT: Brute-force / DGA suspected")
