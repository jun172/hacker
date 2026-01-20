from scapy.all import sniff, Raw
from collections import Counter
import math

# =========================
# バイト頻度解析
# =========================
def byte_frequency(data, top=8):
    freq = Counter(data)
    return freq.most_common(top)

# =========================
# エントロピー計算
# =========================
def entropy(data):
    freq = Counter(data)
    length = len(data)
    return -sum((c/length) * math.log2(c/length) for c in freq.values())

# =========================
# XORっぽいか簡易チェック
# =========================
def xor_detect(data):
    results = []
    for key in range(256):
        decoded = bytes(b ^ key for b in data)
        if all(32 <= c <= 126 for c in decoded[:20]):
            results.append((key, decoded[:30]))
    return results[:3]  # 出すのは最大3件

# =========================
# パケット解析本体
# =========================
def analyze_packet(pkt):
    if not pkt.haslayer(Raw):
        return

    data = pkt[Raw].load
    size = len(data)

    print("\n" + "="*50)
    print(f"[+] Payload size: {size} bytes")

    # HEX表示（先頭だけ）
    print("[HEX]", data[:32].hex())

    # バイト頻度
    print("[Byte Frequency]")
    for b, c in byte_frequency(data):
        print(f"  {hex(b)} : {c}")

    # エントロピー
    e = entropy(data)
    print(f"[Entropy] {round(e, 2)}")

    # エントロピー判定
    if e > 7:
        print("[!] High entropy → 暗号化 or トンネリング疑い")
    elif e < 3:
        print("[!] Low entropy → 平文 or 弱暗号")

    # XOR検知
    xor_results = xor_detect(data)
    if xor_results:
        print("[!] XOR-like pattern detected:")
        for key, decoded in xor_results:
            print(f"    key={key} => {decoded}")

# =========================
# sniff 実行
# =========================
print("[*] Packet sniffing started (Ctrl+C to stop)")
sniff(
    iface="en0",          # Mac Wi-Fi
    prn=analyze_packet,
    store=0
)