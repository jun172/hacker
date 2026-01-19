from scapy.all import sniff, TCP, IP
from collections import defaultdict
import time 

WINDOW = 10
SYN_THRESHOLD = 200
IP_THRESHOLD = 50

syn_count = 0
ip_counter = defaultdict(int)
start_time = time.time()

def analyze(pkt):
    global syn_count, start_time
    
    if pkt.haslayer(TCP) and pkt.haslayer(IP):
        tcp = pkt[TCP]
        ip = pkt[IP]
    
        if tcp.flags == "S":
            syn_count += 1
            ip_counter[ip.src] += 1
            
    if time.time() - start_time > WINDOW:
        evaluate()
        reset()

def evaluate():
    unique_ips = len(ip_counter)
    
    print("\n-- Traffic Analysis ---")
    print(f"SYN packets : {syn_count}")
    print(f"Unique IPs : {unique_ips}")
    
    score =0
    if syn_count > SYN_THRESHOLD:
        score += 50
    if unique_ips > IP_THRESHOLD:
        score += 50
        
    print(f"DDoS risk score : {score}/100")
    
    if score >= 80:
        print("⚠️  Possible SYN Flood Attack Detected")
    elif score >= 40:
        print("🟡 Abnormal traffic")
    else:
        print("🟢 Normal traffic")
        
def reset():
    global syn_count, ip_counter, start_time
    syn_count = 0
    ip_counter = defaultdict(int)
    start_time = time.time()
    
print("Monitoring network traffic...")
sniff(prn=analyze, store=False)