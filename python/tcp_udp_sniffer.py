import socket

def tcp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0",9000))
    s.listen(5)
    print("[TCP] listening on 9000")
    
    while True:
        conn, addr = s.accept()
        print("[TCP] connection from {addr}")
        conn.close()
        
def udp_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("0.0.0.0",9001))
    print("[UDP] listening on 9001")
    
    while True:
        data, addr = s.recvfrom(1024)
        print(f"[UDP] packet from {addr}")
        
#並列起動
import threading
threading.Thread(target=tcp_server, daemon=True).start()
threading.Thread(target=udp_server, daemon=True).start()

while True:
    pass