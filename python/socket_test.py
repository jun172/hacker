import socket 
target = "127.0.0.1"
port = 80

s = socket.socket()
result = s.connect_ex((target, port))

if result == 0:
    print("ポートが開いている")
else:
    print("閉じている")
s.close
