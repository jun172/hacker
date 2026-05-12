import socket
import random
import struct
import time

SERVER = ("127.0.0.1", 1054)

def build_query(domain):
    tid = random.randint(0, 65535)
    flags = 0x0100
    qdcount = 1

    header = struct.pack(">HHHHHH", tid, flags, qdcount, 0, 0, 0)

    qname = b""
    for part in domain.split("."):
        qname += bytes([len(part)]) + part.encode()
    qname += b"\x00"

    question = qname + struct.pack(">HH", 1, 1)
    return header + question

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("[*] Raw DNS brute-force simulator started")

while True:
    domain = f"rand{random.randint(10000,99999)}{random.randint(10000,99999)}.local"
    packet = build_query(domain)
    sock.sendto(packet, SERVER)
    time.sleep(0.03)
