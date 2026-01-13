# 1️⃣ SQLインジェクションっぽい文字列検出
sql_input = input("文字列を入力してください: ")
if "' OR 1=1 --" in sql_input:  # 部分一致で検出
    print("不正入力: SQLインジェクションの可能性あり")
else:
    print("入力OK")

# 2️⃣ access.log からIP出現回数判定
from collections import Counter
import re

ip_list = []

with open("server.log", "r", encoding="utf-8") as f:
    for line in f:
        ips = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", line)
        ip_list.extend(ips)

ip_counter = Counter(ip_list)

for ip, count in ip_counter.items():
    if count >= 5:
        print(f"{ip} は {count} 回出現 → 不正アクセスの可能性")
    else:
        print(f"{ip} は {count} 回出現 → 正常")

# 3️⃣ メールアドレス形式判定
email = input("メールアドレスを入力してください: ")
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
if re.match(pattern, email):
    print(f"{email} は有効なメールアドレスです")
else:
    print(f"{email} は無効なメールアドレスです")

# 4️⃣ ランダム12文字パスワード生成
import random
import string

chars = string.ascii_letters + string.digits
password = "".join(random.choice(chars) for _ in range(12))
print("生成されたパスワード:", password)

# 5️⃣ 任意Pythonコード実行（危険モジュールブロック）
code = input("Pythonコードを入力してください: ")
blocked_modules = ["os", "sys", "subprocess", "shutil"]

if any(mod in code for mod in blocked_modules):
    print("危険なコードが含まれているため実行できません")
else:
    exec(code)


# フローチャート（コメント付き）
#
# ┌─────────────────────────────┐
# │      1. SQLインジェクション判定      │
# │ ユーザー入力を取得                  │
# │ 入力に "' OR 1=1 --" が含まれる？ │
# │   ├─ Yes → "不正入力" を表示      │
# │   └─ No  → "入力OK" を表示        │
# └─────────────────────────────┘
#               │
#               ▼
# ┌─────────────────────────────┐
# │      2. access.log IP監視        │
# │ access.log を1行ずつ読み込み     │
# │ 正規表現でIP抽出                 │
# │ Counterで出現回数を集計         │
# │ count >= 5？                     │
# │   ├─ Yes → "不正アクセスの可能性"│
# │   └─ No  → "正常" を表示        │
# └─────────────────────────────┘
#               │
#               ▼
# ┌─────────────────────────────┐
# │      3. メールアドレス判定       │
# │ ユーザー入力を取得                │
# │ 正規表現にマッチするか？         │
# │   ├─ Yes → "有効" を表示        │
# │   └─ No  → "無効" を表示        │
# └─────────────────────────────┘
#               │
#               ▼
# ┌─────────────────────────────┐
# │      4. ランダムパスワード生成    │
# │ 英大小文字＋数字の文字列を作成   │
# │ 12文字をランダムに選ぶ          │
# │ 生成されたパスワードを表示      │
# └─────────────────────────────┘
#               │
#               ▼
# ┌─────────────────────────────┐
# │      5. exec安全実行             │
# │ ユーザーコードを取得             │
# │ 危険モジュールが含まれるか？     │
# │   ├─ Yes → "実行不可" を表示    │
# │   └─ No  → execでコード実行     │
# └─────────────────────────────┘
#               │
#               ▼
# ┌─────────────────────────────┐
# │           終了                  │
# └─────────────────────────────┘
