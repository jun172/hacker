fail_count = int(input("ログイン失敗回数:"))
if fail_count >= 3:
    print("アカウントロック")
else:
    print("ログイン可能")

age = int(input("年齢:"))
hour =int(input("時間(0-23):"))

if age >= 18 and 10 <= hour <= 20:
    print("入場可能")
else:
    print("入場不可能")

#権限別に表示画面変更
role = input("権限:")

if role == "管理者権限":
    print("管理者画面")
elif role == "編集者":
    print("編集画面")
else:
    print("閲覧画面")

score = int(input("点数:"))
attenddance = input("出席あり？(y/n):")

if score >= 90 and attenddance == "y":#yならばスコア90以上かつ出席y
    print("優")
elif score >= 70 and attenddance == "y":
    print("良")
elif score >= 60:
    print("可")
else:
    print("不可能")

stock =int(input("在庫数:"))
can_ship = input("配送可能?(y/n):")

if stock > 0 and can_ship == "y":
    print("注文可")
else:
    print("注文不可能")

#会員ランク別特典
rank = input("会員ランク(S/A/B)")

if rank == "S":
    print("特権1")
elif rank =="A":
    print("特権2")
else:
    print("特権3")
    
#残高＋限度額チェック
balance = int(input("残高:"))
limit = int(input("限度額:"))

if balance >= limit:
    print("利用可能")
else:
    print("利用不可能")

#ログインと権限管理（セキュア）
users = {
    "admin": {"pw":"1234","role":"管理者"},
    "user1": {"pw":"abcd","role":"一般"}
}
#ログイン処理
userneme = input("ID:")
password =input("pw:")

if userneme in users and password == users[userneme]["pw"]:
    print("ログイン成功")
    role = users[userneme]["role"]
    if role == "管理者":
        print("管理者画面アクセス可")
    else:
        print("一般ユーザー画面アクセス可")
else:
    print("ログイン失敗")

stock = int(input("在庫数:"))
balance = int(input("所持金:"))
price = int(input("商品価格:"))
member = int(input("会員ですか？(y/n):"))

if stock > 0:
    if balance >= price:
        if member == "y":
            print("購入可.会員特権あり")
        else:
            print("購入可")
    else:
        print("残高不足")
else:
    print("在庫なし")
    
#年齢＋時間帯で入場可否
age = int(input("年齢:"))
hour = int(input("時間(0-23):"))

if age >= 18:
    if 10 <= hour <= 20:
        print("入場可能")
    else:
        print("営業時間外")
else:
    print("未成年は入場不可")

#パスワード強度判定（セキュリティ）
password = input("パスワードを入力:")

if len(password) >= 8:
    if any(c.isdigit() for c in password):
        if any(c.isupper() for c in password):
            print("強いパスワード")
        else:
            print("中パスワード(大文字なし)")
    else:
        print("中パスワード(数字なし)")
else:
    print("弱いパスワード")
    
#Lv5複合条件サンプル（総合）
logged_in = input("ログイン済み?(y/n):")
role = input("権限(admin/user):")
age = int(input("残高:"))
stock = int(input("在庫:"))

if logged_in == "y":
    if role == "admin":
        print("管理者画面アクセス可")
        if age >= 18:
            print("成年確認OK")
    else:
        print("一般画面アクセス")
    if stock > 0 and balance >= 1000:
        print("購入可")
    else:
        print("購入不可能")
else:
    print("ログいしてください")
#簡単TCPサーバー
import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost',12345))
s.listen()

conn, addr =s.accept()
data = conn.recv(1024)
conn.send(b"Hello")
conn.close()

#Pythonで requests を使ったHTTPリクエスト（GET / POST）
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)
#ステータスコード確認
print("ステータスコード:",response.status_code)
data = response.json()
print("レスポンス:",data)

