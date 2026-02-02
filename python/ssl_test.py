import ssl
import socket

context = ssl.create_default_context()

with socket.create_connection(("example.com",443)) as sock:
    with context.wrap_socket(sock, server_hostname="example.com") as ssock:
        ssock.sendall(b"GET / HTTP/1.1\r\nHOost: example/com\r\n\r\n")
        print(ssock.recv(1024))
