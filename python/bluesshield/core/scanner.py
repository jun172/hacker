import sys
import socket
from urllib.parse import urlparse
from utils import banner
from dns_enum import enumerate_dns
from ssl_analyzer import analyze_ssl
from dir_enum import dir_enum

def parse_target(target):
    if not target.startswith("http"):
        target = "http://" + target

    parsed = urlparse(target)
    host = parsed.hostname
    port = parsed.port

    if port is None:
        port = 443 if parsed.scheme == "https" else 80

    return parsed.scheme, host, port

def is_port_open(host, port):
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((host, port))
        s.close()
        return True
    except:
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python scanner.py http://target:port")
        return

    scheme, host, port = parse_target(sys.argv[1])

    banner("DNS ENUMERATION")
    enumerate_dns(host)

    banner("PORT CHECK")
    if not is_port_open(host, port):
        print(f"Port {port} closed.")
        return
    else:
        print(f"Port {port} open.")

    if scheme == "https":
        banner("SSL ANALYSIS")
        analyze_ssl(host, port)
    else:
        print("Skipping SSL (HTTP detected)")
        base_url = f"{scheme}://{host}:{port}"
        dir_enum(base_url)

    banner("SCAN COMPLETE")

if __name__ == "__main__":
    main()
