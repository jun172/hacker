import random
import time

# ===== 攻撃者の挙動を再現 =====

def random_ip():
    return ".".join(str(random.randint(1,254)) for _ in range(4))

def rand_port():
    return random.randint(1024, 65535)

class SynFloodSimulator:
    def __init__(self, target_ip, target_port):
        self.target_ip = target_ip
        self.target_port = target_port
        self.events = []

    def send_syn(self):
        pkt = {
            "src_ip": random_ip(),
            "src_port": rand_port(),
            "dst_ip": self.target_ip,
            "dst_port": self.target_port,
            "flags": "SYN",
            "time": time.time()
        }
        self.events.append(pkt)

    def run(self, count):
        print(f"[SIM] Simulating SYN flood to {self.target_ip}:{self.target_port}")
        for i in range(count):
            self.send_syn()
        print(f"[SIM] {count} SYN packets simulated")

    # ===== 防御側（IDS） =====
    def detect(self, threshold=50):
        ip_counter = {}
        for e in self.events:
            ip_counter[e["src_ip"]] = ip_counter.get(e["src_ip"], 0) + 1

        suspicious = [ip for ip, c in ip_counter.items() if c > threshold]

        print("\n[IDS] Detection result")
        print("Total packets:", len(self.events))
        print("Unique source IPs:", len(ip_counter))
        print("Suspicious IPs:", suspicious if suspicious else "None")

# ===== 実行 =====
if __name__ == "__main__":
    target = input("Target IP: ")
    port = int(input("Target Port: "))
    count = int(input("Simulated packet count: "))

    sim = SynFloodSimulator(target, port)
    sim.run(count)
    sim.detect()
