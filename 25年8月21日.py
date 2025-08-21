# ===============================
# サイバー攻撃系・解析系 実習まとめ
# ===============================
import re
import hashlib
import random
import string

# 1. 入力 -> 条件分離 -> 出力
num = int(input('数値を入力してください: '))
if num > 0:
    print('正の数')
elif num < 0:
    print('負の数')
else:
    print('ゼロ')

# 2. ファイル処理 -> 出力
with open("access.log", "r", encoding="utf-8") as f:
    data = f.read()
    print("=== access.log の内容 ===")
    print(data)

# 3. モジュール -> ファイル処理 -> IP抽出
ip_address = []
with open("access.log", "r", encoding="utf-8") as f:
    for line in f:
        ips = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", line)
        ip_address.extend(ips)
print("検出されたIP:", set(ip_address))

# 4. SQLインジェクション風ワード検知
user_input = input("文字を入力してください: ")

def detect_sql(keyword: str, text: str):
    if keyword in text.upper():
        print(f"危険ワード '{keyword}' が含まれています！")
    else:
        print("安全な文字列です")

detect_sql("DROP TABLE", user_input)

# 5. パスワード強度判定 (長さ)
with open("users.txt", "r", encoding="utf-8") as f:
    for pw in f:
        pw = pw.strip()
        if len(pw) < 8:
            print(f"{pw}: 弱いパスワード")
        else:
            print(f"{pw}: 強いパスワード")

# 6. ファイル内容をハッシュ化して保存
with open("config.txt", "r", encoding="utf-8") as f:
    config = f.read()

hashed = hashlib.sha512(config.encode()).hexdigest()
with open("config_hashed.txt", "w", encoding="utf-8") as f:
    f.write(hashed)
print("config.txt をハッシュ化して保存しました")

# 7. URL安全性判定
url = input("URLを入力してください: ")
if url.startswith("http://"):
    print("⚠ 安全ではない通信")
elif url.startswith("https://"):
    print("✅ 暗号化通信")
else:
    print("不明なURL形式です")

# 8. ランダムパスワード生成
def generate_password(size=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(size))

print("自動生成パスワード:", generate_password(12))

# 9. access.logからIP一覧出力
ip_list = []
with open("access.log", "r", encoding="utf-8") as f:
    for line in f:
        ips = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", line)
        ip_list.extend(ips)
print("access.log 内の全IP:", set(ip_list))

# 10. 回文判定
string_input = input("回文判定する文字列を入力してください: ")
if string_input == string_input[::-1]:
    print("回文です")
else:
    print("回文ではありません")
