import socket
import time
from collections import defaultdict

DNS_PORT = 1054          # ← 衝突回避
WINDOW = 10              # 秒
ALERT_SCORE = 70         # 警戒ライン

ip_logs = defaultdict(list)
global_logs = []

print(f"[*] Python DNS IDS with Scoring started on UDP {DNS_PORT}")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", DNS_PORT))

def extract_domain(data):
    idx = 12
    labels = []
    while True:
        length = data[idx]
        if length == 0:
            break
        idx += 1
        labels.append(data[idx:idx+length].decode(errors="ignore"))
        idx += length
    return ".".join(labels)

while True:
    data, addr = sock.recvfrom(512)
    src_ip = addr[0]
    now = time.time()

    domain = extract_domain(data)
    print(f"[QUERY] {src_ip} -> {domain}")

    # --- ログ保存 ---
    ip_logs[src_ip].append((now, domain))
    ip_logs[src_ip] = [(t,d) for t,d in ip_logs[src_ip] if now - t <= WINDOW]

    global_logs.append((now, src_ip, domain))
    global_logs[:] = [(t,i,d) for t,i,d in global_logs if now - t <= WINDOW]

    # ======================
    # スコアリング
    # ======================
    score = 0

    uniq_domains_ip = len(set(d for _, d in ip_logs[src_ip]))
    uniq_domains_all = len(set(d for _,_, d in global_logs))
    uniq_ips = len(set(i for _, i,_ in global_logs))
    total_queries_ip = len(ip_logs[src_ip])

    # 単一IP要素
    score += uniq_domains_ip * 5
    score += total_queries_ip * 2

    # 分散要素
    if uniq_ips >= 5:
        score += uniq_ips * 4
        score += uniq_domains_all * 3

    print(f"[SCORE] IP:{src_ip} Score:{score}")

    if score >= ALERT_SCORE:
        print("🚨 ALERT: Suspicious DNS activity detected!")
        print(f"    IPs: {uniq_ips}")
        print(f"    Domains: {uniq_domains_all}")
        print(f"    Score: {score}")
        print("-" * 40)
