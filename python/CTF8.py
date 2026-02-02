import socket
import random
import time

HOST = '0.0.0.0'
PORT = 10007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# サーバーの最初のメッセージを受信
data = s.recv(1024).decode()
print(data)

# Seed を取得
seed_line = [line for line in data.split("\n") if "Seed:" in line][0]
seed = int(seed_line.split("Seed: ")[1])
print("Seed:", seed)

# 乱数をサーバーと同じシードで再現
random.seed(seed)

for i in range(5):
    guess = random.randint(1, 100)
    print(f"Round {i+1} guess:", guess)
    s.sendall(f"{guess}\n".encode())
    response = s.recv(1024).decode()
    print(response)

# FLAG が出力される
final_response = s.recv(1024).decode()
print(final_response)

s.close()
