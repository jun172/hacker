import pyshark

INTERFACE = "en0"  # 実際のインターフェースに変更
CAPTURE_TIME = 10   # まず10秒でテスト

print(f"[*] Capturing on {INTERFACE} for {CAPTURE_TIME} seconds...")

capture = pyshark.LiveCapture(interface=INTERFACE)
capture.sniff(timeout=CAPTURE_TIME)

if len(capture) == 0:
    print("[!] No packets captured. Check interface, permissions, and network traffic.")
else:
    print(f"[+] Captured {len(capture)} packets:")
    for packet in capture[:5]:  # 最初の5パケットだけ表示
        print(packet)
