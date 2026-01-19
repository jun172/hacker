from scapy.all import sniff, TCP, IP, Raw
import threading
from queue import Queue
from datetime import datetime
from collections import defaultdict
import time

# ========= 設定 =========
LOG_FILE = "log.txt"
REPORT_FILE = "report.txt"

# Snort風シグネチャ（IoTで多い攻撃）
RULES = [
    ("Telnet attempt", b"telnet"),
    ("Suspicious POST", b"POST"),
    ("Remote shell", b"whoami"),
    ("Command exec", b"bash"),
    ("Downloader", b"wget"),
    ("Downloader", b"curl"),
]

stats = defaultdict(int)
event_q = Queue()

# ========= ログ =========
def log_alert(text):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} {text}\n")

# ========= アラート処理 =========
def handle_alert(name, src, dst):
    msg = f"[ALERT] {name} {src} -> {dst}"
    print(msg)
    log_alert(msg)
    stats[name] += 1

# ========= パケット検査 =========
def inspect(packet):
    if packet.haslayer(TCP) and packet.haslayer(Raw) and packet.haslayer(IP):
        payload = packet[Raw].load.lower()
        for name, sig in RULES:
            if sig in payload:
                src = packet[IP].src
                dst = packet[IP].dst
                event_q.put((name, src, dst))

# ========= ワーカー =========
def worker():
    while True:
        name, src, dst = event_q.get()
        handle_alert(name, src, dst)
        event_q.task_done()

# ========= 日次レポート =========
def daily_report_loop():
    while True:
        time.sleep(60 * 60 * 24)
        with open(REPORT_FILE, "a") as f:
            f.write(f"\n=== Daily Report {datetime.now().date()} ===\n")
            for k, v in stats.items():
                f.write(f"{k}: {v}\n")
        stats.clear()

# ========= メイン =========
if __name__ == "__main__":
    print("[*] IoT Mini IDS started (Local Logging Mode)")

    for _ in range(4):
        threading.Thread(target=worker, daemon=True).start()

    threading.Thread(target=daily_report_loop, daemon=True).start()
    
    sniff(iface="lo0", filter="tcp", prn=inspect, store=0)