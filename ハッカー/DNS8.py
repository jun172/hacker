import socket, time, math, subprocess
from collections import defaultdict, Counter

DNS_PORT = 1054
WINDOW = 5
BLOCK_THRESHOLD = 80
RATE_THRESHOLD = 50

records = defaultdict(list)   # ip -> [(t, domain, entropy, nxd)]
global_events = []             # (t, ip, entropy)

def entropy(s):
    c = Counter(s)
    l = len(s)
    return -sum((n/l)*math.log2(n/l) for n in c.values())

def is_link_local(ip):
    return ip.startswith("169.254.")

def block_ip(ip):
    print(f"🛑 BLOCK {ip}")
    subprocess.run(["pfctl", "-t", "botnet", "-T", "add", ip],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", DNS_PORT))

print("[*] Botnet DNS IDS/IPS started")

while True:
    data, addr = sock.recvfrom(512)
    ip, sport = addr
    if is_link_local(ip): 
        continue

    # --- domain parse ---
    idx = 12
    labels = []
    while idx < len(data) and data[idx] != 0:
        l = data[idx]
        idx += 1
        labels.append(data[idx:idx+l].decode(errors="ignore"))
        idx += l
    domain = ".".join(labels)

    e = entropy(labels[0]) if labels else 0
    nxd = True  # 自作DNSなので未登録はNX扱い
    now = time.time()

    records[ip].append((now, domain, e, nxd))
    global_events.append((now, ip, e))

    # --- window cleanup ---
    records[ip] = [r for r in records[ip] if now - r[0] <= WINDOW]
    global_events[:] = [g for g in global_events if now - g[0] <= WINDOW]

    # --- scoring ---
    uniq = len(set(r[1] for r in records[ip]))
    avg_e = sum(r[2] for r in records[ip]) / len(records[ip])
    nxd_ratio = sum(r[3] for r in records[ip]) / len(records[ip])

    same_entropy_ips = len(set(g[1] for g in global_events if abs(g[2]-avg_e) < 0.3))

    score = 0
    score += uniq * 1.2
    score += avg_e * 15
    score += nxd_ratio * 30
    score += same_entropy_ips * 5

    print(f"[BOT] {ip} uniq={uniq} ent={avg_e:.2f} nxd={nxd_ratio:.2f} peers={same_entropy_ips} score={int(score)}")

    if score >= BLOCK_THRESHOLD:
        block_ip(ip)
    elif score >= RATE_THRESHOLD:
        print(f"⚠ RATE LIMIT {ip}")
