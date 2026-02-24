from scapy.all import sniff, TCP,IP
from collections import defaultdict
from datetime import datetime, timedelta

WINDOW = 10
SYN_THRESHOLD = 100
RATIO_THRESHOLD = 3

stats = defaultdict(lambda:{
    "syn":0,
    "synack":0,
    "timestamps":[]
})

def detect(packet):
    if packet.haslayer(TCP):
        tcp = packet[TCP]
        ip = packet[IP]
        src = ip.src
        now =datetime.now()
        
        record =stats[src]
        
        if tcp.plags == "S":
            record["syn"] += 1
            record["timestamps"].append(now)
            
        elif tcp.flags == "SA":
            record["synack"] += 1
            
        # 古いデータ削除
        record["timestamps"] =[
            t for t in record["timestamps"]
            if now -t < timedelta(seconds=WINDOW)
        ]
        
        if len(record["timestamps"]) > SYN_THRESHOLD:
            ratio = record["syn"] / (record["synack"] + 1)
            
            if ratio > RATIO_THRESHOLD:
                print(f"[ALERT] SYN flood suspected from {src}")
                
sniff(filter="tcp",prn=detect)