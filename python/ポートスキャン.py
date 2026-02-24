import socket
def scan_port(host,port):
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((host,port))
        print(f"[OPEN] {port}")
    except:
        pass
    finally:
        s.close()
        
for p in [80,443,22,8080]:
    scan_port("example.com")