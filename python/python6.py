import socket
from concurrent.futures import ThreadPoolExecutor

TIMEOUT = 1

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(TIMEOUT)
            result = s.connect_ex((target, port))
            if result == 0:
                return port
    except:
        pass
    return None

def scan_target(target, ports):
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, target, p) for p in ports]
        for f in futures:
            result = f.result()
            if result:
                open_ports.append(result)
    return open_ports


if __name__ == "__main__":
    target = "192.168.1.10"
    ports = range(1, 1025)
    result = scan_target(target, ports)

    print("Open Ports:", result)
