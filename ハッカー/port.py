import socket
def scan_port(ip,port,timeout=0.5):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((ip, port))
        s.close()
        return True
    except:
        return False
    
ip = "127.0.0.1"
port = 1053

if scan_port(ip, port):
    print(f"[OPEN] {ip}:{port}")
else:
    print(f"[CLOSED] {ip}:{port}")