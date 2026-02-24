import socket 
from utils import log

COMMON_SUBDOMAINS =[
    "www","mail","dev","test","admin"
]

def enumerate_dns(domain):
    results = []
    log(f"DNS enumeration for {domain}")

    for sub in COMMON_SUBDOMAINS:
        full = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(full)
            log(f"[FOUND] {full} -> {ip}")
            results.append((full, ip))
        except socket.gaierror:
            pass

    return results