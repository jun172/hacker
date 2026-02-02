from scapy.all import IP, ICMP, sr1

packet = IP(dst="8.8.8.8") / ICMP()
response = sr1(packet, timeout=2)

if response:
    print("応答あり")
else:
    print("応答なし")
