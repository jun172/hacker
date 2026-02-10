import socket 

target = "127.0.0.1"
ports = [22,23,80,443,3389,8081]

for port in ports:
    s = socket.socket()
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} open")
    s.close()