from scapy.all import sniff, TCP, IP
from collections import defaultdict
from datetime import datetime, timedelta

# 設定
THRESHOLD = 100          # SYN回数
WINDOW_SECONDS = 10      # 監視時間窓（秒）

syn_counter = defaultdict(list)

def alert(ip, count):
    print(f"[ALERT] SYN Flood detected | src={ip} | syn_count={count}")

def packet_handler(pkt):
    if IP in pkt and TCP in pkt:
        tcp = pkt[TCP]

        # SYN=1, ACK=0 → 新規接続要求
        if tcp.flags == "S":
            src_ip = pkt[IP].src
            now = datetime.now()

            # 時間窓外を削除
            syn_counter[src_ip] = [
                t for t in syn_counter[src_ip]
                if now - t < timedelta(seconds=WINDOW_SECONDS)
            ]

            syn_counter[src_ip].append(now)

            if len(syn_counter[src_ip]) >= THRESHOLD:
                alert(src_ip, len(syn_counter[src_ip]))
                syn_counter[src_ip].clear()

print("[SOC] SYN Flood detector started")
sniff(filter="tcp", prn=packet_handler, store=False)
