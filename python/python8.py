import socket
from concurrent.futures import ThreadPoolExecutor

TIMEOUT = 1

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(TIMEOUT)
            if s.connect_ex((target, port)) == 0:
                return port
    except:
        pass
    return None


def threaded_scan(target, ports, threads=100):
    open_ports = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(scan_port, target, p) for p in ports]
        for f in futures:
            result = f.result()
            if result:
                open_ports.append(result)

    return open_ports
