import socket
import threading

def scan(port):
    try:
        s = socket.socket()
        s.settimeout(0.3)
        s.connect(("127.0.0.1",port))
        print(f"[OPEN] {port}")
        s.close()
    except:
        pass
    
for port in range(1,1025):
    t = threading.Thread(target=scan, args=(port,))
    t.start()