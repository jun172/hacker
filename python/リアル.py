from scapy.all import sniff, TCP, UDP, IP

def packet_handler(pkt):
    if IP in pkt:
        src = pkt[IP].src
        dst = pkt[IP].dst
        
        if TCP in pkt:
            print(f"[TCP] {src} -> {dst} | sport={pkt[TCP].sport} dport={pkt[TCP].dport}")
            
        elif UDP in pkt:
            print(f"[UDP] {src} -> {dst} | sport={pkt[UDP].sport} dport={pkt[UDP].dport}")
print("[SOC] TCP/UDP monitor started")
sniff(prn=packet_handler, store=False)