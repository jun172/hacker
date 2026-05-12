# fake_bot_dns.py
import random
import string
import socket
import time

DNS_SERVER = "127.0.0.1"   # 自分のDNS監視先
PORT = 1054

def random_domain():
    name = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
    return f"{name}.local"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    domain = random_domain()
    print(f"[BOT] query => {domain}")
    sock.sendto(domain.encode(), (DNS_SERVER, PORT))
    time.sleep(0.1)
