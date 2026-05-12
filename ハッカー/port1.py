import socket
TARGET = "127.0.0.1"
PORTS = range(1, 1025)

for port in PORTS:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)
    try:
        s.connect((TARGET, port))
        print(f"[OPEN] {port}")
        s.close()
    except:
        pass