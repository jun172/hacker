import socket
def scan_udp(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1)
    try:
        s.sendto(b"\x00",(ip, port))
        data, _ = s.recvfrom(1024)
        return True
    except socket.timeout:
        return False
    except:
        return False

if scan_udp("127.0.0.1",1053):
    print("[UDP OPEN] 1053")
else:
    print("[NO RESPONSE] 1053")
    

print("PORT STATE")
print("-----------")

for port in range(1, 1025):
    if scan_udp("127.0.0.1",port):
        print(f"{port}/tcp open")