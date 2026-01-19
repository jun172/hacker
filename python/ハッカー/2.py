# agent.py
import socket
import subprocess

ALLOWED = ["whoami", "pwd", "ls","cd .."]

s = socket.socket()
s.connect(("192.168.10.111", 9901))


while True:
    cmd = s.recv(1024).decode()
    if cmd == "exit":
        break

    if cmd not in ALLOWED:
        s.send(b"[BLOCKED] command not allowed")
        continue

    result = subprocess.getoutput(cmd)
    s.send(result.encode())

s.close()
