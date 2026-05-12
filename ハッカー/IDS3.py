import socket 
import time 
from collections import defaultdict, deque

LISTEN_IP = "0.0.0.0"
LISTEN_PORT = 1054
UPSTRESM_DNS = ("8.8.8.8",53)

WINDOW = 30
MIN_QUERIES = 20
NXDOMAIN_THRESHOLD = 0.7

stats = defaultdict(lambda: deque())

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((LISTEN_IP, LISTEN_PORT))
sock.settimeout(1)

print(f"[*] DNS Forwarding IDS staetd on UDP {LISTEN_PORT}")

def get_qname(data):
    qname = ""
    i = 12
    while i < len(data):
        length = data[i]
        if length == 0:
            break
        qname += data[i+1:i+1+length].decode(errors="ignore") + "."
        i += length + 1
    return qname[:-1]

def get_recode(data):
    return data[3] & 0x0F

while True:
    try:
        data, addr = sock.recvfrom(512)
    except socket.timeout:
        continue
    
    src_ip = addr[0]
    qname= get_qname(data)
    
    # 上流DNSへ転送
    upstream = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    upstream.sendto(data, UPSTRESM_DNS)
    response, _ =  upstream.recvfrom(512)
    upstream.close()
    
    rcode = get_recode(response)
    nxdomain = (rcode == 3)
    
    now = time.time()
    stats[src_ip].append((now, nxdomain))
    
    while stats[src_ip] and now -stats[src_ip][0][0] > WINDOW:
        stats[src_ip].popleft()
        
    total = len(stats[src_ip])
    nx = sum(1 for _, nx in stats[src_ip] if nx)
    ratio = nx / total if total else 0
    
    print(f"[QUERY] {src_ip} -> {qname} | NXDOMAIN={nxdomain}")
    
    if total >= MIN_QUERIES and ratio >= NXDOMAIN_THRESHOLD:
        print(f"🚨 ALERT DNS BRUTEFORCE {src_ip} "
               f"NXDOMAIN {nx}/{total} ({ratio:.2f})")
        
    sock.sendto(response, addr)