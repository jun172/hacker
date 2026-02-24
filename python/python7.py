from scapy.all import IP, ICMP, sr1
import socket

def is_host_alive(target):
    packet = IP(dst=target)/ICMP()
    reply = sr1(packet, timeout=1, verbose=0)

    if reply and reply.haslayer(ICMP):
        return True
    return False

if __name__ == "__main__":
    target = "192.168.1.10"
    if is_host_alive(target):
        print(f"{target} is alive")
    else:
        print(f"{target} is down")
