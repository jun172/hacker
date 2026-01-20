import socket
import random
import string
import time

TARGET_IP   = "127.0.0.1"
TARGET_PORT = 1054     # あなたの IDS
INTERVAL    = 0.05     # 攻撃速度（小さいほど速い）

def random_domain():
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{name}.local"

def build_dns_query(domain):
    transaction_id = random.randint(0, 65535).to_bytes(2, "big")
    flags = b'\x01\x00'  # standard query
    qdcount = b'\x00\x01'
    ancount = b'\x00\x00'
    nscount = b'\x00\x00'
    arcount = b'\x00\x00'

    header = transaction_id + flags + qdcount + ancount + nscount + arcount

    question = b''
    for part in domain.split('.'):
        question += bytes([len(part)]) + part.encode()
    question += b'\x00'          # end
    question += b'\x00\x01'      # A record
    question += b'\x00\x01'      # IN

    return header + question

print("[*] DNS Attack Simulator started")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    domain = random_domain()
    packet = build_dns_query(domain)

    sock.sendto(packet, (TARGET_IP, TARGET_PORT))
    print(f"[ATTACK] Sent query for {domain}")

    time.sleep(INTERVAL)
