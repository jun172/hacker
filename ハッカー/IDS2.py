import socket 
import time 
from collections import defaultdict, deque

DNS_PORT = 1054
WINDOW = 10 #秒
MIN_QUERIES = 20
NXDOMAIN_THRESHOLD = 0.8

#ログ構造
stats = defaultdict(lambda: deque())

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0",DNS_PORT))

print("[*] DNS IDS (NXDOMAIN Ratio) started on UDP",DNS_PORT)

while True:
    data, addr = sock.recvfrom(512)
    client_ip = addr[0]
    now = time.time()
    
    #ドメイン名抽出
    idx = 12
    labels = []
    while data[idx] != 0:
        l = data[idx]
        idx += 1
        labels.append(data[idx:idx+l].decode(errors="ignore"))
        idx += l
    domain = ".".join(labels)
    
    #DNS応答レコード
    rcode = data[3] & 0x0F #下位
    is_nxdomain = (rcode == 3)
    
    print(f"[QUERY] {client_ip} -> {domain} | NXDOMAIN={is_nxdomain}")
    
    #ログ保存
    stats[client_ip].append((now, is_nxdomain))
    
    #古いログ削除
    while stats[client_ip] and now - stats[client_ip][0][0] > WINDOW:
        stats[client_ip].popleft()
        
    total = len(stats[client_ip])
    nx = sum(1 for _, nxd in stats[client_ip] if nxd)
    
    if total >= MIN_QUERIES:
        ratio = nx / total 
        
        if ratio >= NXDOMAIN_THRESHOLD:
            print("🚨 [ALERT] DNS Brute-force suspected")
            print(f" IP:{client_ip}")
            print(f"    NXDOMAIN ratio: {nx}/{total} = {ratio:.2f}")