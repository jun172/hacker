import socket 
import ssl

HOST = '127.0.0.1'
PORT = 8443

#通常のソケット
sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#SSLコンテキスト作成（クライアント用）
context = ssl.create_default_context()

#ソケットをSSL化して接続
ssl_sock =context.wrap_socket(sock, server_hostname=HOST)
ssl_sock.connect((HOST, PORT))

# データ送信
ssl_sock.send(b"Hello Server!")
data = ssl_sock.recv(1024)
print("受信:", data.decode())

ssl_sock.close()