# -----------------------------
# ログイン試行・パスワード生成・設定ファイルハッシュ化・URL判定
# -----------------------------

import string
import secrets
import hashlib
import os

# 1. ログイン試行 (3回まで)
# -------------------------------------
# 正しいユーザー名とパスワードを固定値で用意
correct_user = "admin"
correct_pass = "1234"

# 入力を受け取る
username = input("名前を入力してください: ")
password = input("パスワードを入力してください: ")

# 3回まで間違えられる仕組み
for i in range(1, 4):  # range(1,4) = 1,2,3
    if username == correct_user and password == correct_pass:
        print("ログイン成功")  # 両方正しい場合は成功
        break
    else:
        print(f"{i}回間違えました")
        if i == 3:  # 3回目も失敗なら終了
            print("ログイン不可能")

print("\n")


# 2. 安全なパスワード生成
# -------------------------------------
# 英大文字 + 英小文字 + 数字を組み合わせてランダム生成
def pass_gen(size=12):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(secrets.choice(chars) for _ in range(size))

print("自動生成パスワード:", pass_gen(10))  # 長さ10のパスワード
print("\n")


# 3. config.txt のパスワードをハッシュ化
# -------------------------------------
config_path = "config.txt"

if os.path.exists(config_path):  # ファイルが存在するか確認
    with open(config_path, "r", encoding="utf-8") as f:
        plaintext = f.read().strip()  # 中身を読み取り（余計な改行は除去）
        hashed = hashlib.sha256(plaintext.encode()).hexdigest()  # SHA256でハッシュ化

    # ハッシュ化したものを上書き保存
    with open(config_path, "w", encoding="utf-8") as f:
        f.write(hashed)

    print("平文パスワードをハッシュ化しました。")
else:
    print("config.txt は存在しません。")

print("\n")


# 4. URL が https か確認
# -------------------------------------
# input() は文字列なので int() に変換しない（←ここが前の間違い）
url = input("URLを入力してください: ")

# startswith() で文字列の頭を判定
if url.startswith("http://"):
    print("暗号化されていません")
elif url.startswith("https://"):
    print("暗号化されています")
else:
    print("エラー: URL形式が正しくありません")

print("\n")


# 5. 最終確認: 正しいユーザー情報を持つ辞書
# -------------------------------------
# 実際のログイン認証に使える形式（キーと値のペア）
user_data = {"user": "admin", "password": "1234"}
print("ユーザー情報:", user_data)


# 開始
  # │
  # ▼
# ユーザー名とパスワード入力
  # │
  # ▼
 # ┌──────────────┐
 # │  3回まで認証 │
 # │  (正しい? ) │
 # └──────────────┘
  # │Yes                  │No
  # ▼                     # ▼
# ログイン成功       # 失敗回数+1 → 3回?
                        # │
                      # Yes│
                        # ▼
                   # ログイン不可能

# ─────────────────────────────

  # ▼
# 安全なパスワード生成 (secretsで12桁)
  # │
  # ▼
# 生成したパスワードを表示

# ─────────────────────────────

  # ▼
# config.txt存在確認
  # │Yes                │No
  # ▼                   # ▼
# 平文パス読込 → SHA256化    # 「存在しません」表示
  # │
  # ▼
# ハッシュ値を config.txt に保存

# ─────────────────────────────

  # ▼
# URLを入力
  # │
  # ▼
 # ┌───────────────┐
 # │ URL判定       │
 # │ http:// ?     │─→ # 暗号化なし
 # │ https:// ?    │─→ # 暗号化あり
 # │ それ以外      │─→ # エラー
 # └───────────────┘

# ─────────────────────────────

  # ▼
# ユーザー情報辞書を表示
  # │
  # ▼
# 終了
