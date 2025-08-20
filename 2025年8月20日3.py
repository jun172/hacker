# -----------------------------
# フローチャートコメント
# -----------------------------

# 1. data.txt から "nember" を含む行を抽出
# [開始] → [data.txt を1行ずつ読む] → [line.lower()に'nember'が含まれる?]
#     → はい → print(line) → 次の行へ
#     → いいえ → 次の行へ
# [全行終了] → [終了]

# 2. log.txt の内容を全て表示
# [開始] → [log.txt を読む] → [ファイル内容を print] → [終了]

# 3. パスワード SHA256 ハッシュ化
# [開始] → [ユーザー入力: password] → [hashlib.sha256(password.encode()).hexdigest()]
# → [ハッシュ値を出力] → [終了]

# 4. users.csv から username を表示
# [開始] → [users.csv を DictReader で読み込み]
# → [1行ずつ row["username"] を出力] → [全行終了] → [終了]

# 5. 入力文字列が回文か判定
# [開始] → [文字列入力 s] → [s == s[::-1]?]
#     → はい → print("回文です")
#     → いいえ → print("回文ではありません")
# [終了]


# -----------------------------
# まとめ処理：ファイル抽出・ログ読み込み・パスワードハッシュ化・CSV読み込み・回文判定
# -----------------------------

import hashlib
import csv

# 1. data.txt から "nember" を含む行を抽出
print("=== data.txt 内 'nember' を含む行 ===")
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        if "nember" in line.lower():  # 小文字化して判定
            print(line.strip())
print("\n")

# 2. log.txt の内容を全て表示
print("=== log.txt の内容 ===")
with open("log.txt", 'r', encoding="utf-8") as f:
    file_content = f.read()
    print(file_content)
print("\n")

# 3. パスワードを SHA256 でハッシュ化
password = input("パスワードを入力してください: ")
hashkey = hashlib.sha256(password.encode()).hexdigest()
print("SHA256ハッシュ化:", hashkey)
print("\n")

# 4. users.csv から username を取り出して表示
print("=== users.csv 内のユーザー名 ===")
with open("users.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["username"])
print("\n")

# 5. 入力文字列が回文か判定
string = input("回文判定する文字列を入力してください: ")

def check_palindrome(s):
    if s == s[::-1]:
        print("回文です")
    else:
        print("回文ではありません")

check_palindrome(string)
