import socket
import time
import math
from collections import defaultdict, deque, Counter

# -----------------------------
# 設定
# -----------------------------
DNS_PORT = 1054       # 監視ポート
WINDOW = 10           # 秒単位の統計ウィンドウ
ENTROPY_THRESHOLD = 3.0
UNIQ_THRESHOLD = 20

# -----------------------------
# データ格納
# -----------------------------
stats = defaultdict(lambda: deque())

# -----------------------------
# エントロピー計算関数
# -----------------------------
def entropy(s: str) -> float:
    if not s:
        return 0.0
    c = Counter(s)
    return -sum((v / len(s)) * math.log2(v / len(s)) for v in c.values())

# -----------------------------
# ソケット作成
# -----------------------------
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", DNS_PORT))
print(f"[*] DNS5 IDS started on UDP {DNS_PORT}")

# -----------------------------
# メインループ
# -----------------------------
while True:
    try:
        data, addr = sock.recvfrom(512)
        now = time.time()
        src_ip, src_port = addr

        # --- DNSドメイン名解析 ---
        idx = 12  # DNSヘッダ12バイト後から質問セクション
        domain_parts = []
        while idx < len(data):
            l = data[idx]
            if l == 0:
                break
            idx += 1
            domain_parts.append(data[idx:idx+l].decode(errors="ignore"))
            idx += l
        domain = ".".join(domain_parts)
        subdomain = domain.split(".")[0] if domain else ""
        ent = entropy(subdomain)

        # --- 統計更新 ---
        stats[src_ip].append({"t": now, "domain": domain, "entropy": ent})

        # ウィンドウ外データ削除
        stats[src_ip] = deque([x for x in stats[src_ip] if now - x["t"] < WINDOW])

        # --- 特徴量 ---
        uniq_domains = len(set(x["domain"] for x in stats[src_ip]))
        avg_entropy = sum(x["entropy"] for x in stats[src_ip]) / len(stats[src_ip])

        # --- ログ表示 ---
        print(f"[DNS5] {src_ip}:{src_port} domain={domain}")
        print(f"      uniq={uniq_domains} avg_entropy={avg_entropy:.2f}")

        # --- アラート判定 ---
        if uniq_domains > UNIQ_THRESHOLD and avg_entropy > ENTROPY_THRESHOLD:
            print(f"🚨 DNS5 ALERT: Brute-force / DGA suspected from {src_ip}")

    except KeyboardInterrupt:
        print("[*] Exiting...")
        break
    except Exception as e:
        print(f"[!] Error: {e}")
