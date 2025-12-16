#!/usr/bin/env python3
"""
extract_domains.py

依存:
  pip install pyshark
  sudo apt install tshark
"""

import pyshark, time
from collections import defaultdict

pcap_file = ""  # 解析するPCAPファイル
max_packets = 0            # 0で全パケット

# 端末(mac/ip) -> set(domains)
access_map = defaultdict(set)

cap = pyshark.FileCapture(pcap_file, only_summaries=False)

for i, pkt in enumerate(cap):
    if max_packets and i >= max_packets:
        break

    src = getattr(pkt, 'ip.src', None) or getattr(pkt, 'eth.src', None) or getattr(pkt, 'wlan.sa', None)
    if not src:
        continue

    # DNSクエリ
    dns_q = getattr(pkt, 'dns.qry_name', None)
    if dns_q:
        access_map[src].add(dns_q)
        continue

    # TLS SNI
    sni = getattr(pkt, 'tls.handshake_extensions_server_name', None) or getattr(pkt, 'ssl.handshake_extensions_server_name', None)
    if sni:
        access_map[src].add(sni)
        continue

# 出力
for device, domains in access_map.items():
    print(f"Device: {device}")
    for d in sorted(domains):
        print(f"  -> {d}")
    print()
