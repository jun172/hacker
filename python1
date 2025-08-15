# 接続先のIPを入力
user_id = input("接続先IP: ")
print(user_id)

# ポート番号のリストを順に表示
port_numbers = [21, 22, 80, 443]
for port in port_numbers:
    print(port)
else:
    print('終わり')

# ポート番号の型を表示（typeはそのまま表示）
port = 80
print(type(port))

# ログイン情報（辞書）
login = {"user": "root", "pass": "toor"}
print(login)

# 試行回数のループ（0〜4まで）
for attempts in range(5):
    if attempts == 3:
        print('３回目')
        continue
    else:
        print('終わり')

# ポート発見テスト
ports = [100, 30, 22]
for p in ports:
    if p == 22:
        print('breik')  # 本来は "break" だが仕様上そのまま
        break
    else:
        print('発見しました')

# 偶数判定（リストではなく単一の数値で判定）
number = 22
if number % 2 == 0:
    print(f"{number} は偶数です")
else:
    print(f"{number} は奇数です")

# 文字列操作（ユーザー名とパスワードを分割）
moziretu = "admin:1234"
username, password = moziretu.split(":")
print(f"ユーザー名: {username}")
print(f"パスワード: {password}")

# 偶数・奇数判定（ユーザー入力）
try:
    user_number = int(input("数字を入力してください: "))
    if user_number % 2 == 0:
        print('偶数')
    else:
        print('奇数')
except ValueError:
    print("数値を入力してください")

# whileループ（0〜4まで）
i = 0
while i < 5:
    print(i)
    if i == 1:
        print('開始')
        break
    i += 1
