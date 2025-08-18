# -----------------------------
# 基礎問題（ウォーミングアップ）
# -----------------------------

# 1. 変数の計算
x = 7
c = x * 2
print(c)   # → 14

# 2. リストの合計
mylist = [3, 6, 9]
print(sum(mylist))   # → 18

# 3. 偶数判定（0〜9）
for i in range(0, 10):
    if i % 2 == 0:
        print(i, 'は偶数')

# 4. 文字列を大文字に変換
sont = 'heijffbsjc'
print(sont.upper())  # → HEIJFFBSJC

# 5. 二乗関数
def square(n):
    return n ** 2

print(square(2))   # → 4


# -----------------------------
# 案件型ハッキング問題
# -----------------------------

# 6. ログイン認証
user_id = input('ユーザー名: ')
password = input('パスワード: ')
if user_id == "admin" and password == "1234":
    print("ログイン成功")
else:
    print("ログイン失敗")

# 7. log.txt の内容を表示
with open("log.txt", 'r', encoding="utf-8") as f:
    file = f.read()
    print("== log.txt ==")
    print(file)

# 8. SQL Injection 簡易検知
user = input('入力: ')
if "DROP TABLE" in user:
    print('SQL Injectionの可能性あり')

# 9. パスワードをSHA256でハッシュ化
import hashlib
password = input("パスワードを入力: ")
hs = hashlib.sha256(password.encode()).hexdigest()
print(hs)

# 10. URL判定
url = input("URLを入力してください: ")
if url.startswith("http://"):
    print("これはHTTPです")
elif url.startswith("https://"):
    print("これはHTTPSです")
else:
    print("不明なURLです")

# 11. ファイル操作
path = 'data/src/test.txt'
with open(path) as f:
    line = f.readline()
    print(type(line))   # <class 'str'>
    print(line)

# 12. 辞書アクセス
myaccent = {"id": 1, "mail": 2, "pass": 3}
print(myaccent["mail"])   # → 2

# 13. パスワード逆順
pas = input('パスワード: ')
print(pas[::-1])

# 14. 危険文字検知
use = input('入力: ')
if ";" in use or "'" in use:
    print("危険文字あり")

# 15. 簡易ブルートフォース (a〜z 4桁総当たり)
import string
words = list(string.ascii_lowercase)
passwords = []
for word_1 in words:
    for word_2 in words:
        for word_3 in words:
            for word_4 in words:
                passwords.append(word_1 + word_2 + word_3 + word_4)
print("生成パターン数:", len(passwords))  # 456,976 通り

# 16. ポート番号の危険度判定
port = int(input("ポート番号: "))
if port == 80:
    print("80番ポート → Web(HTTP) → 中リスク")
elif port == 22:
    print("22番ポート → SSH → 高リスク")
elif port == 443:
    print("443番ポート → HTTPS → 低リスク")
else:
    print("未知のポート")

# 17. パスワード強度チェック
core = input("パスワードを入力: ")
if any(c.isupper() for c in core) and any(c.islower() for c in core) and any(c.isdigit() for c in core):
    print("強いパスワード")
elif any(c.isalpha() for c in core) and any(c.isdigit() for c in core):
    print("中程度のパスワード")
else:
    print("弱いパスワード")

# 18. 平文パスワードを検出してハッシュ化して保存
import os
config = input("平文パスワード: ")
def save_file_at_dir(dir_path, filename, file_content, mode='w'):
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, filename), mode) as f:
        f.write(file_content)

hashed_config = hashlib.sha256(config.encode()).hexdigest()
save_file_at_dir("output", "config_hashed.txt", hashed_config)
print("パスワードをハッシュ化して保存しました。")


from collections import Counter
import re

#ログファイル開く
with open ("acces.log","r",encoding="utf-8")as f:
    logs=f.readlines()
    
ips=[]

#各行からIPアドレスから抽出
for line in logs:
    match=re.match(r"(\d+\.\d+\.\d+\.\d+)",line)
    if match:
        ips.append(match.group(1))
#IPアドレス出現
count=Counter(ips)

#最も多いIP
most_common_ip, count=Counter.most_common(1)[0]

print("最もアクセスの多いIP:",most_common_ip)
print("アクセス回数:",count)

