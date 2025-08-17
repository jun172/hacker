# ユーザーから入力を受け取る
menu = input("username: ")

# 入力チェック
if not menu:
    print("null（入力がありません）")
else:
    print("文字あり")

    # 入力内容をファイルに追記
    with open("chat_log.txt", "a", encoding="utf-8") as f:
        print(menu, file=f)

# ログファイルを読み込んで表示
with open("chat_log.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print("=== chat_log.txt の内容 ===")
    print("".join(lines))


# ユーザー入力と辞書検索
user_input = input('ユーザー名を入力してください: ')
user_dict = {"nakai": "jun125"}

if user_input in user_dict:
    print('ありました')
else:
    print('ありませんでした')


# ポートスキャン風（1〜1023まで偶数だけ"open"表示）
for i in range(1, 1024):
    if i % 2 == 0:
        print(i, 'open')


# 集合（set）の書き方修正
ip = {"192.168.1.1", "192.168.0.2"}  # 波括弧 {} 内は文字列にする
print(type(ip))
print(ip)


# ファイルオープンの基本
path = 'data/src/log.txt'

try:
    f = open(path)
    print(type(f))
    f.close()
except FileNotFoundError:
    print("ファイルが見つかりません")

# with を使うと自動でcloseされる
try:
    with open(path) as f:
        print(type(f))
except FileNotFoundError:
    print("ファイルが見つかりません")


# パスワード入力チェック
password = input('8桁の英数字を入力してください: ')
if len(password) >= 8 and password.isalnum():
    print("OK: 英数字8桁以上")
else:
    print("NG: 条件を満たしていません")


# 辞書の値を取得
key = {"名前": 1026, "id": 3017}
val = key["名前"]
print(val)


# ネストループ（hostとportを組み合わせ）
hosts = ['8036']
ports = ['9165']

for h in hosts:
    for p in ports:
        print(h, p)
        if h == '8036' and p == '9165':
            print('表示')
            break


# try-except例
try:
    x = ['190.682.389']
    print(x)
except Exception as e:
    print('エラー発生:', e)


# ネストループの break 制御
flag = False
for i in range(100):
    for j in range(100):
        if i > j > 70:
            flag = True
            break
        print(i, j)
    if flag:
        break


# リスト内包表記
result = [x**2 for x in range(1, 11)]
print(result)

    