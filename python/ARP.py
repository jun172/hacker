import pyshark
import requests

INTERFACE = "en0"  # macOS の Wi-Fi は通常 en0
CAPTURE_TIME = 20   # 秒

def lookup_vendor(mac):
    """MACアドレスからベンダー名を取得"""
    try:
        r = requests.get(f"https://api.macvendors.com/{mac}", timeout=5)
        return r.text if r.status_code == 200 else "Unknown"
    except:
        return "Unknown"

def capture_macs(interface, timeout):
    """指定時間ネットワークをキャプチャしてMACアドレスを取得"""
    print(f"[*] Capturing on {interface} for {timeout} seconds...")
    capture = pyshark.LiveCapture(interface=interface)
    capture.sniff(timeout=timeout)

    macs = set()
    for pkt in capture:
        if hasattr(pkt, 'eth'):
            macs.add(pkt.eth.src)  # 送信元MACを追加
            macs.add(pkt.eth.dst)  # 宛先MACも追加

    return macs

def main():
    macs = capture_macs(INTERFACE, CAPTURE_TIME)
    print(f"[*] Found {len(macs)} unique MAC addresses\n")

    for mac in macs:
        vendor = lookup_vendor(mac)
        print(f"{mac} -> {vendor}")

if __name__ == "__main__":
    main()
