import hashlib
import json

# 1. 数値判定
num = float(input("数値を入力してください: "))
if num >= 0:
    print("OK")
else:
    print("NG")


# 2. DROP 判定
text = input("文字列を入力してください: ")
if "DROP" in text:
    print("危険な入力")
else:
    print("安全な入力")


# 3. パスワードを SHA256 でハッシュ化
password = input("パスワードを入力してください: ")
hashed = hashlib.sha256(password.encode()).hexdigest()
print("SHA256ハッシュ:", hashed)


# 4. users.json の username を表示
with open("users.json", mode="r", encoding="utf-8") as f:
    data = json.load(f)
    print("username:", data.get("username"))


# 5. log.txt から error 行だけ抽出
with open("log.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        if "error" in line.lower():   # 大文字小文字を無視
            print(line.strip())


# 6. ポート番号判定
port = int(input("ポート番号を入力してください: "))
if port == 22:
    print("SSH")
elif port == 80:
    print("HTTP")
elif port == 443:
    print("HTTPS")
else:
    print("不明なポート")


# 7. 簡易パスワード強度判定
password = input("もう一度パスワードを入力してください: ")
has_digit = any(ch.isdigit() for ch in password)
has_lower = any(ch.islower() for ch in password)
has_upper = any(ch.isupper() for ch in password)

if password.isdigit():
    print("弱い（数字だけ）")
elif has_digit and has_lower and has_upper:
    print("強い（英字＋数字＋大文字）")
elif has_digit and (has_lower or has_upper):
    print("中くらい（英字＋数字）")
else:
    print("判定不能")


# 8. config.txt を自動でハッシュ化保存
with open("config.txt", mode="r", encoding="utf-8") as f:
    content = f.read().strip()

# 平文（英数字のみ）だったらハッシュ化して上書き
if not all(ch in "0123456789abcdef" for ch in content) or len(content) != 64:
    hashed = hashlib.sha256(content.encode()).hexdigest()
    with open("config.txt", mode="w", encoding="utf-8") as f:
        f.write(hashed)
    print("config.txt をハッシュ化して保存しました")
else:
    print("すでにハッシュ済み")


# 9. URL 判定
url = input("URLを入力してください: ")
if url.startswith("https://"):
    print("暗号化通信")
elif url.startswith("http://"):
    print("安全でない通信")
else:
    print("不明なURL")


# 10. ログイン認証
correct_user = "admin"
correct_pass = "1234"

username = input("ユーザー名: ")
password = input("パスワード: ")

if username == correct_user and password == correct_pass:
    print("ログイン成功")
else:
    print("ログイン失敗")

