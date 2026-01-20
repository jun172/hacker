import socket
import time
import math
import os
from collections import defaultdict, deque

#設定
DNS_PORT = 1054
WINDOW = 5 #秒
RATE_LIMIT_THRESHLD = 50
RATE_LIMIT_DELAY = 0.2 #秒
BLOCK_THRESHOLD =80
WHITELIT = {"127.0.0.1"}
BLOCKED = set()

# 状態管理
logs = defaultdict(lambda: deque())

#エントロビー
def entropy(s):
    if not s:
        return 0
    prob = [s.count(c) / len(s) for c in set(s)]
    return -sum(p * math.log2(p) for p in prob)
#pfでIP切断
def block_ip(ip):
    if ip in WHITELIT:
        return 
    print(f"⛔ BLOCK IP (OS): {ip}")
    os.system(f"sudo pfctl -t blocklist -T add {ip}")
    BLOCKED.add(ip)

def parse_domain(data):
    idx = 12
    labels = []
    while True:
        l = data[idx]
        if l == 0:
            break
        idx += 1
        labels.append(data[idx:idx+l].decode(errors="ignore"))
        idx += l
    return ".".join(labels)

#メイン
print("[*] DNS IDS + IPS started on UDP", DNS_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0",DNS_PORT))

while True:
    data, addr = sock.recvfrom(512)
    ip = addr[0]
    now = time.time()
    
    domain = parse_domain(data)
    sub = domain.split(".")[0]
    
    #ログイン追加
    logs[ip].append((now, domain))
    
    #WINDIW外消す
    while logs[ip] and now - logs[ip][0][0] > WINDOW:
        logs[ip].popleft()
        
    domain = [d for _, d in logs[ip]]
    uniq = len(set(domain))
    ent =entropy(sub)
    
    #スコアリング
    score = 0
    if uniq > 10:
        score += 30
    if ent > 3.5:
        score += 40
    if len(domain) > 20:
        score += 20
    
    print(f"[QUERY] {ip} -> {domain} | uniq={uniq} ent={ent:.2f}　score={score}")
    
    #判定
    if score >= BLOCK_THRESHOLD and ip not in BLOCKED:
        block_ip(ip)
        continue
    elif score >= RATE_LIMIT_THRESHLD:
        print(f"⚠ RATE LINIT {ip}")
        time.sleep(RATE_LIMIT_DELAY)
        
    #ダミー応答
    try:
        sock.sendto(data, addr)
    except:
        pass