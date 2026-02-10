import asyncio
import psutil
import subprocess
import json
import time

WS_URL = "ws://localhost:8765"
TRAFFIC_LIMIT = 10 * 1024 * 1024  # 10MB
TARGET_HOST = "8.8.8.8"

# --- アラート送信（今回はprintで代用可） ---
async def send_alert(message):
    print(f"[ALERT] {message}")

# --- Ping疎通確認 ---
def ping_check():
    result = subprocess.run(
        ["ping", "-c", "1", TARGET_HOST],
        stdout=subprocess.DEVNULL
    )
    return result.returncode == 0

# --- 通信量取得 ---
def get_traffic():
    net = psutil.net_io_counters()
    return net.bytes_sent + net.bytes_recv

# --- Nmapスキャン ---
def nmap_scan():
    result = subprocess.check_output(
        ["nmap", "-p", "22,23,3389", "localhost"]
    ).decode()
    return "open" in result

# --- 自動遮断 ---
def block_traffic():
    print("🚫 通信遮断実行")
    subprocess.run(["sudo", "iptables", "-A", "OUTPUT", "-j", "DROP"])

# --- メイン監視 ---
async def monitor():
    prev_traffic = get_traffic()

    while True:
        await asyncio.sleep(5)

        current = get_traffic()
        diff = current - prev_traffic
        prev_traffic = current

        if diff > TRAFFIC_LIMIT:
            await send_alert("通信量閾値超過 → 遮断")
            block_traffic()
            break

        if nmap_scan():
            await send_alert("危険ポート検出 → 遮断")
            block_traffic()
            break

# --- 起動 ---
async def main():
    if not ping_check():
        await send_alert("ネットワーク疎通不可")
        return

    await monitor()

asyncio.run(main())
