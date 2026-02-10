import socket
import subprocess
import re
import requests
import ipaddress

# -------------------------
# Wi‑Fi ローカルIP
# -------------------------
def get_private_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

# -------------------------
# グローバルIP
# -------------------------
def get_global_ip():
    return requests.get("https://api.ipify.org", timeout=5).text

# -------------------------
# 接続中Wi‑FiのBSSID
# -------------------------
def get_bssid():
    output = subprocess.check_output(
        ["system_profiler", "SPAirPortDataType"]
    ).decode()
    match = re.search(r"BSSID: ([0-9a-fA-F:]{17})", output)
    return match.group(1) if match else None

# -------------------------
# MAC → メーカー
# -------------------------
def lookup_vendor(mac):
    if not mac:
        return "Unknown"
    try:
        r = requests.get(
            f"https://api.macvendors.com/{mac}",
            timeout=5
        )
        return r.text if r.status_code == 200 else "Unknown"
    except:
        return "Unknown"

# -------------------------
# LAN内 IP & MAC 取得（ARP）
# -------------------------
def get_lan_devices():
    devices = []
    output = subprocess.check_output(["arp", "-a"]).decode()

    for line in output.splitlines():
        # 例: ? (192.168.1.1) at a4:cf:12:xx:xx:xx on en0
        match = re.search(
            r"\(([\d\.]+)\) at ([0-9a-f:]{17})",
            line,
            re.IGNORECASE
        )
        if match:
            ip, mac = match.groups()
            devices.append((ip, mac))
    return devices

# -------------------------
# メイン
# -------------------------
if __name__ == "__main__":
    private_ip = get_private_ip()
    global_ip = get_global_ip()
    bssid = get_bssid()
    ap_vendor = lookup_vendor(bssid)
    network = ipaddress.ip_network(private_ip + "/24", strict=False)

    print("===== Wi‑Fi / Network Info =====")
    print("Private IP:", private_ip)
    print("Global IP:", global_ip)
    print("LAN Network:", network)
    print("AP BSSID:", bssid)
    print("AP Manufacturer:", ap_vendor)

    print("\n===== LAN Devices (IP / MAC / Vendor) =====")
    devices = get_lan_devices()
    for ip, mac in devices:
        vendor = lookup_vendor(mac)
        print(f"{ip:15} {mac}  {vendor}")
