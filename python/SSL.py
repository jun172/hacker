import socket
import ssl

# サーバー用設定
HOST = '127.0.0.1'
PORT = 8443

#通常のソケット作成
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(5)
print("サーバー起動 (TLS)")

# SSLコンテキスト作成
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.crt", keyfile="server.key") # 証明書と秘密鍵

while True:
    client_sock, addr = sock.accept()
    print("接続:",addr)
    
    #ソケットをSSL化
    ssl_client =  context.wrap_socket(client_sock, server_side=True)
    
    data = ssl_client.recv(1024).decode()
    print("受信:",data)
    
    ssl_client.send(b"Hello Secure World!")
    ssl_client.close()