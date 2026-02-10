import socket
import requests
import ipaddress

def get_rivete_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def get_global_ip():
    return requests.get("https://api.ipify.org").text

private_ip = get_rivete_ip()
global_ip = get_global_ip()
network = ipaddress.ip_network(private_ip + "/24", strict=False)

print("Scanning LAN:", network)
print("Private IP (LAN):",private_ip)
print("Global IP (WAN):", global_ip)