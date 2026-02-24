from scapy.all import ARP, sniff
from collections import defaultdict
import pandas as pd
from datetime import datetime

# ARPテーブル履歴
arp_history = defaultdict(list)

def detect_arp_spoof(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2:  # is-at
        ip = packet[ARP].psrc
        mac = packet[ARP].hwsrc
        now = datetime.now()

        # 履歴更新
        arp_history[ip].append((mac, now))

        # MACが以前と違う場合
        macs = [m for m, t in arp_history[ip]]
        if len(set(macs)) > 1:
            print(f"[ALERT] Possible ARP spoofing! IP {ip} has multiple MACs: {set(macs)}")
