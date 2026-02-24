from collections import defaultdict
import time

scan_tracker = defaultdict(list)

def detect_port_scan(src_ip, dst_port):
    now = time.time()
    scan_tracker[src_ip].append((dst_port, now))

    scan_tracker[src_ip] = [
        x for x in scan_tracker[src_ip]
        if now - x[1] < 5
    ]

    unique_ports = len(set(p for p, _ in scan_tracker[src_ip]))

    if unique_ports > 20:
        return {
            "type": "PORT_SCAN",
            "src_ip": src_ip,
            "mitre": "T1046"
        }

