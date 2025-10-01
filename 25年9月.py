# ① パスワードが8文字以上かつ数字を含むか判定
use=input("パスワード:")
if len(use)>=8 and any (c.isdigit() for c in use):#8文字長さと数字を含む
    print("パスワードは8文字以上かつ数字を含む")
else:
    print("パスワード条件に満たしていません")

# ② ユーザー名に不正な文字が含まれていないかチェック
username=input("ユーザー名入力")
illegal_chars=[';','',""]
if any(chr in username for char in illegal_chars):#不正な文字
    print("不正な文字が含まれている")
else:
    print("不正な文字が含まれていません")
# ③ 文字列を SHA-256 でハッシュ化
import hashlib
name=input("文字列を入力:")
hs=hashlib.sha256(name.encode())
print("SHA-256:",hs.hexdigest())
# ④ CSV ファイルを読み込み、ユーザー名とハッシュ化パスワードを辞書に格納
import csv
users={}
with open ("users.csv",newline="",encoding="utf-8") as f:
    reader=csv.reader(f)
    for row in reader:
        username,password=row
        hashed=hashlib.sha256(password.encode()).hexdigest()
        users[username]=hashed
    print(users)
# ⑤ リストにあるユーザー名の存在確認
use_list=["admin","guest","user"]
input_name=input("ユーザー名を入力:")
if input_name in use_list:
    print("名前あります")
else:
    print("ありません")
## ⑥ メールアドレスが正しい形式か判定（簡易チェック）
import re
email =input("メールアドレスを入力")
patten = r"^[\w\.-]+@[\w\.-]+\.\w+$"
if re.match(patten,email):
    print("正しい")
else:
    print("正しくない")
# ⑦ パスワードに辞書攻撃用単語が含まれていないか確認
comm_pasuwood=["123456","passwprd","admin"]
if any(word in use for word in comm_pasuwood):
    print("辞書単語が含まれている")
else:
    print("安全です")
# ⑧ 簡易SQLインジェクションチェック
sql_input=input("SQLの文字列")
dagger_word=["OR 1=1", "' OR '1'='1"]
if any(word in sql_input for word in dagger_word):
    print("SQLインデェクション可能性あり")
else:
    print("問題なし")
# ⑨ ログイン試行回数カウント
login_attempts=0
while login_attempts <3:
    password =input("入力")
    if password != "correct":
        login_attempts+=1
        print(f"試行回数:{login_attempts}")
    else:
        print("成功")
        break
if login_attempts >=3:
    print("アクセス拒否")
# ⑩ HTMLエスケープ
user_input=input("文字列:")
import html
safe_output=html.escape(user_input)
print("安全に表示:",safe_output)





#2️⃣ SQL攻撃・インジェクション対策（11〜20）
import sqlite3
import hashlib
import logging
from datetime import datetime
#SQLiteデータベースにユーザー名とパスワードを安全に挿入するコードを作れ（プレースホルダ使用）。
def inset_user(username,paswword):
    conn=sqlite3.connect("app.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS usre (id INTEGER PRIMRY KEY, username TEXT, password TEXT)")
    cur.execute("INSERT INTO users (username, password) VALUES(?,?)",(username,password))
    conn.commit()
    conn.close()
#SQLクエリでユーザー入力を直接埋め込まず、安全に検索する方法を示せ
def get_user_by_username(username):
    conn=sqlite3.connect("app.db")
    cur=conn.cursor()
    cur.execute("SELCT * FROM users WHERE username =?",(username))
    rows=cur.fetchall()
    conn.close()
    return rows
#ベースからデータを取得する安全な関数を作れ。
def get_user_by_id(user_id):
    conn=sqlite3.connect("app.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM users WHERE id=?",(user_id))
    row=cur.fetchall()
    conn.close()
    return row
# パスワードをハッシュ化してDBに保存する関数を作れ
def hash_password(password: str)->str:
    return hashlib.sha256(password.ecode()).hexdigest()
#DB内のユーザー情報を読み込み、辞書型で返す関数を作れ。
def load_users():
    conn=sqlite3.connect("app.db")
    cur=conn.cursor()
    cur.execute("SELCT id, username, password FROM users")
    rows=cur.fetchall()
    conn.close()
    return [{"id":r[0],"username":r[1],"password":r[2]} for r in rows]

#複数のログイン試行をDBに記録し、攻撃パターンを検出せよ
conn=sqlite3.connect("app.db")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS logins (time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, username TEXT, success INTEGER)")
def log_login(userame,success):
    cur.execute("INSERT INTO logins (username, succes) VALUES(?,?)",(username,success))
    conn.commit()
# 攻撃パターン例: 同じユーザーで失敗が3回以上
cur.execute("SELECT username, COUNT(*) FROM logins WHERE succes=0 GROUP BY username HAVING COUNT(*) >=3")
print("攻撃パターン検出:", cur.fetchall())

#SQLインジェクション文字列が入力された場合はログに記録し警告を出せ。
def detect_sql_injection(input_str):
    suspicious=["--",";","OR","AND"," ' "]
    if any(s in input_str.upper() for s in suspicious):
        logging.warning(f"SQLインジェクション疑い:{input_str}")
        return True
    return False
#DB検索時にLIKE句でワイルドカード攻撃を防ぐ方法を示せ。
def safe_search(term):
    conn=sqlite3.connect("app.db")
    cur=conn.cursor()
    # ワイルドカード文字をエスケープ
    term =term.reples("%","\\%").replace("_","\\_")
    cur.execute("SELECT * FROM users WHERE username LIKE ? '\\'",(f"%{term}%",))
    print(cur.fetchall())
#既存ユーザーを更新する関数で安全にパラメータを渡す方法を示せ。
def update_password(username,new_password):
    cur.execute("UPDATE users SET password=? WHERE username=?",(hash_password(new_password),username))

update_password("test_user","newSecret456")
#データベース接続情報を暗号化して安全に保存する方法を示せ。
from cryptography.fernet import Fernet

# 鍵を生成（1回だけ実行して保存）
key = Fernet.generate_key()
with open("key.key", "wb") as f:
    f.write(key)

# 鍵を読み込む
with open ("key.key","rb") as f:
    key=f.read()
cipher=Fernet(key)
# 接続情報を暗号化して保存
db_info="sqlite:///usre.db" #SQliteデータベース
encrypted =cipher.encrypt(db_info.encode())
with open ("db_info","wb") as f:
    f.write(encrypted)
# 復号
with open ("db_info.enc","rb") as f:
    encrypted_data=f.read()
decrypted=cipher.decrypt(encrypted_data).decode()
print("復号した接続情報:",decrypted)

#3️⃣ Web攻撃対策・解析（21〜25）
#入力フォームからのPOSTデータを受け取り、XSS攻撃を防ぐサニタイズ処理を作れ。
import requests
url = ""
requests=requests.get(url)
print(f"スタートコード:{requests.status_code}")
print(requests.text[:200])
#HTTPリクエストを解析して、スクリプトタグを含む攻撃を検出せよ。
import requests
from bs4 import BeautifulSoup
url = ""
res=requests.get(url)
soup=BeautifulSoup(res.text,"html.解析")
scripts=soup.find_all("script")

if scripts:
    print("⚠️攻撃の可能性:<script>タグを検出しました。")
else:
    print("✅ 安全:<script>タグは見つかりません。")
#Webサーバーログから不審なアクセスを検出するスクリプトを作れ。
import re
import requests
LOG_FILE= "/var/log/apache2/access.log"#リナックスアパッチ必要
SUSPICIOUS_PATTERNS=[
    r"<scrpt>",#XSSぽい
    r"union.*select",#SQLインジェクション
    r"\.\./",#ディレクトリトラバーサル
    r"/etc/paswd"# システムファイルアクセス
    r"wget",#外部取得
    r"curl"#外部取得
]
def detect_suspicious_requests(log_file):
     suspicious_requests = []
     
     with open(log_file,"r",encoding="utf-8",errors="ignore") as f:
         for line in f:
             for pattren in SUSPICIOUS_PATTERNS:
                 if re.search(pattren, line, re.IGNORECASE):
                     suspicious_requests.append(line.strip())
                     break
                 return SUSPICIOUS_PATTERNS
if __name__=="__main__":
    results=detect_suspicious_requests(LOG_FILE)
    
    if results:
        print("🚨不審アクセスを検知しました。")
        for r in results:
            print(r)
        else:
            print("✅ 不審なアクセスは見つかりませんでした。")
#リクエストヘッダに含まれる不正なUser-Agentを検知してログに残せ。
from flask import Flask,request

app=Flask(__name__)
@app.rote("/")
def index():
    ua=request.headers.get("User-Agent","")
    blacklist=["sqlmap","nikto","namp"]#攻撃ツール例
    if any(bad in ua.lower() for bad in blacklist):
        with open("ua_attack.log","a") as f:
            f.write(f"[警告]不正UA検出:{ua}\n")
        return "⚠️ アクセス拒否",403
    return  "✅ 正常アクセス"
if __name__=="__name__":
    app.run(host="0.0.0.0",port=8888)
    
#パケットキャプチャの解析
from scapy.all import sniff,TCP,IP
def packet_callback(packet):
    if TCP in packet:
        print(f"送信元:{packet[IP].src},宛先:{packet[IP]},ポート:{packet[TCP].dport}")

sniff(filter="TCP",prn=packet_callback,count=10)
#XSS対策のサニタイズ処理
import html
def sanitize_input(user_input):
    """
    ユーザー入力をHTMLエスケープしてXSSを防ぐ
    """
    return html.escape(user_input)
# 実際の使用例
user_comment='<script>alrt("危険!")</script>'
safe_comment=sanitize_input(user_comment)
print("元の入力:",user_comment)
print("サニタイズ後",safe_comment)
#4️⃣ ネットワーク・サイバー演習（26〜30）
#受信したHTTPパケットを解析してGETとPOSTを判別せよ。
http_requests=[
    "GET /index.php HTPP/1.1",
    "POST /login.php HTTP/1.1"
]
for req in http_requests:
    if req.startswith("GET"):
        print("GETリクエスト:",req)
    elif req.startswith("POST"):
        print("POSTリクエスト:",req)
#URLリストから脆弱なURL（例: SQLパラメータがあるURL）を抽出せよ。
urls=[
    #this my url
]
for url in urls:
    if "=" in url:
        print("潜在的なコマンドインジェクション文字を検出:{char}")
#入力された文字列に含まれる潜在的なコマンドインジェクション文字（&,;,|）を検出せよ
danger_chars=['&',';','|']
user_input="ls; rm -rf /"
for char in danger_chars:
    if char in user_input:
        print("潜在的な脆弱性URl:",url)
#ローカルネットワーク上のIPアドレスに順番にPingを送り、生存しているホストを検出せよ
import subprocess
import ipaddress

network=ipaddress.IPv4Network("my ipaddrees")

for ip in network.hosts():
    result =subprocess.run(['ping','-c','1','-W',str(ip)],stdout=subprocess.DEVNULL)
    if result.returncode==0:
        print("存在ホスト:",ip)
#特定のポート（例: 22, 80, 443）に対してソケット接続を試み、開放ポートを判定せよ。
import socket
hosts=["自分のホスト"]
ports=[22,80,443]

for host in hosts:
    for port in ports:
        s =socket.socket(socket.AF_inET,socket.SOCK_STREAN)
        s.settimeout(1)
        
        try:
            s.connect((host,port))
            print(f"{host}:{port}解放中")
        except:
            pass
        s.close()
#1️⃣ Flask 基礎（1〜7）
from flask import Flask,request, jsonify,render_tenmplte,session
from flask import redirect,url_for
from flask_session import Session

app=Flask(__name__)
app.Secret_key="supersecret"
app.config["SESSION_TYPE"]="filesystem"
Session(app)
#Flaskアプリを作成し、/ にアクセスしたときに「Hello, World!」と表示せよ。
@app.roure()
def index():
    return "hello World!"
# /greet/<name> にアクセスすると、name を使って挨拶文を返すルートを作れ。
@app.roure("/greet/<name>")
def greet(name):
    return f"こんにちは,{name}さん!"
#POSTメソッドで送信されたフォームデータ（名前と年齢）を受け取り、JSONで返#す。
@app.roure("/from",methods=["POST"])
def form_post():
    name=request.form.get("name")
    age=request.form.grt("age")
    return jsonify({"名前":name,"年齢":age})
#"GETパラメータ ?q=<検索ワード> を受け取り、検索結果ページを表示するルートを作れ。
@app.route("/search")
def search():
    qury=request.args.get("q","")
    return f"検索ワード:{qury}の検索結果を表します。"
#エラーページ（404）をカスタムHTMLで表示せよ。
@app.errorhandler(404)
def page_ot_fond(e):
    return "<h1>404ページが見つかりません</h1>",404
#静的ファイル（CSS, JS）を配置し、HTMLページに適用する方法を示せ。
@app.page("/page")
def page():
    return render_tenmplte("page.html")
#laskでセッションを使ってユーザー名を保存・表示せよ。
@app.route("/login",methpods=["POST"])
def login():
    username=request.form.get(username)
    search["username"]=username
    return redirect(url_for("profile"))
@app.route()
def profile():
    username=search.get("username","ゲスト")
    return f"現在ログイン中のユーザー:{username}"
if __name__=="__main__":
    app.run(debug=True)
#2️⃣ Django 基礎（8〜14）

#見る前に自分のホームディレクトリで環境を直す

#Djangoプロジェクトを作成し、home アプリを作成してトップページを表示せよ。
from django.http import HttpRequest
def home(request):
    return HttpRequest("hello Django!")
#モデル Book(title, author, price) を作成し、マイグレーションを適用せよ。
from django.db import models
class Book(models.book):
    title=models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price=models.CharField()
    
    def __str__(self):
        return self.title
#URLパターン /books/<int:id>/ を作成し、指定IDの書籍情報を表示せよ。
from django import path 
from home import views
urlpatterns=[
    path('',views.home,name='home'),
    path('books/<int:id>/',views.book_detail,name='book_detail')
]
#フォームからユーザーが入力したデータをモデルに保存するビューを作れ。
from django.shortcuts import render,redirect
from .forms import BookForm
def add_book(request):
    if request.method=="POST":
        form =BookForm(request.POST)
        if form.is_vaild():
            form.sava()
            return redirect("home")
    else:
        form=BookForm()
        return render(request,"add_book.html",{"form":form})  
#クラスベースビュー（CBV）でリスト表示ページを作れ。
from django .views.generic import ListView
from .models import Book

class BookListView(ListView):
    model=Book
    template_name="book_list.html"
    context_object_name="books"
#Djangoテンプレートで条件分岐とループを用いて書籍一覧を表示せよ。
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.book_list, name='book_list'),
]

#3️⃣ FastAPI / API開発（15〜20）
#FastAPIで /items/{item_id} ルートを作成し、item_id を返すAPIを作れ。
from fastapi import FastAPI
app=FastAPI()
@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id:tem_id"}
#POSTメソッドでJSONデータを受け取り、バリデーション後に返すAPIを作れ。
from pydantic import BasModel
class GreetiyingModel(BaseeModel):
    texts:str
@app.post("/test_post")
async def text_post(item:GreetiyingModel):
    return {"received_text":item.tests}
#Pydanticモデルを使ってユーザー情報（名前, 年齢, email）を受け取るAPIを作れ。
class UserModel(BaseModel):
    name:str
    age:int
    email:str
@app.post("/user_info")
async def receive_user(user:UserModel):
    return {"name":user.name,"age":user.age,"email":user.email}
#FastAPIでCORS設定を行い、外部サイトからのリクエストを許可せよ。
@app.get("/hello")
async def hello():
    return {"message": "CORSが有効なFastAPIです"}
#🛡 Python × サイバー攻撃系 練習問題 10問
#SQLインジェクション対策  ユーザー入力を直接 SELECT クエリに埋め込むと危険になる理由を説明し、安全に検索するコードを書け。
import sqlite3
conn=sqlite3.connect(":memory")
c=conn.cursor()
c.execute("CREATE TABLE users (id INTEGER, name TEXT)")
c.execute("INSERT INTO users VALUES (1,'Alice')")
c.execute("INSERT INTO users VALUES (2,'Bob')")
conn.comit()

user_input =input("名前を入力:")
c.execute("SELECT * FROM users WHERE name=?,(user_input)")
result=c.fetchall()
print(result)
conn.close()
#XSS対策 入力された文字列をHTMLに出力するプログラムを作り、エスケープ処理をしてXSSを防げ。
import html

user_input=input("コメントを入力:")
safe_input=html.escape(user_input)
print(f"<p>{safe_input}</p>")
#ブルートフォース攻撃シミュレーション 簡単なログイン処理を作り、辞書攻撃リスト ["1234","password","admin"] を使って突破を試みるプログラムを書け。
password=["1234","pasworrd","admin"]
correct_password="password"
for attempt in password:
    if attempt == correct_password:
        print("ログイン成功:",attempt)
        break
    else:
        print("失敗:",attempt)
#DoSシミュレーション（簡易版）requests を使って同じURLに連続アクセスする処理を作り、過負荷攻撃の危険性を確認せよ（※実際には安全なローカルサーバーで実験すること）。
import requests
target="URL"
for i in range(5):
    try:
        r=request.get(target)
        print("アクセス成功",r.status_code)
    except:
        print("アクセス失敗")
#パスワード強度チェック 入力されたパスワードが「8文字以上」「大文字・小文字・数字・記号を含むか」を判定する関数を作れ。
import re
def check_password_strength(password:str)->str:
    if len(password) < 8:
        return "パスワードは8文字以上にしてください"
    # 大文字・小文字・数字・記号をチェック
    if not re.search(r'[A-Z]', password):
        return "大文字が含まれていません"
    if not re.search(r'[a-z]', password):
        return "小文字が含まれていません"
    if not re.search(r'\d', password):
        return "数字が含まれていません"
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "記号が含まれていません"
    
    return "パスワードは強力です"

user_input = input("パスワードを入力: ")
print(check_password_strength(user_input))
#ハッシュ化と総当たり攻撃 パスワードを SHA-256 でハッシュ化し、総当たり（brute force）で短いパスワードを解読するプログラムを書け。
import itertools
import string
import hashlib

target_password="Ab1!"
target_hash=hashlib.sha256(target_password.encode()).hexdigest()

char=string.ascii_letters + string.digits + "!@#"
for length in range(2,5):
    for attempt in itertools.product(char,repeat=length):
        attempt_str=''.join(attempt)
        if hashlib.sha256(attempt_str.encode()).hexdigest()== target_hash:
            print("解読成功:",attempt_str)
            break
#ポートスキャン(安全版） socket モジュールを使って、指定IPの 20〜100 番ポートが開いているかチェックするスクリプトを作れ。
import socket
target_ip="IPアドレス"
star_port=20
end_port=100

for port in range(star_port,end_port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(0.5)
    
result=sock.connect_ex((target_ip,port))
if result ==0:
    print(f"Port{port}is open")
else:
    print(f"Port{port}is closed")
    sock.close()
#ログイン試行制限 ログインを3回間違えたら「アカウントロック」と表示する処理を書け。
correct_password="secret"
max_attempts="9"

for attempt in range(max_attempts):
    user_input==input("パスワード入力")
    if user_input == correct_password:
        print("ログインできました")
        break
    else:
        print(f"パスワードが違います。残りは{max_attempts - attempt-1}回")
else:
    print("ログインできませんでした")
#入力フィルタリング ユーザー入力に ; や ' などの文字が含まれていたら「不正入力」と判定するプログラムを書け。
invalid_chrs=[";","'","'"]
user_input=input("入力")
if any(char in user_input for char in invalid_chrs):
    print("不正")
else:
    print("入力OK")
#セッションID生成 ランダムで一意のセッションIDを uuid または secrets モジュールで生成し、辞書に保存する仕組みを作れ。
import secrets
import json
session_id=secrets.token_urlsafe(16)
date={"session_id":session_id}# 辞書に保存
with open ("session.json","w")as f:
    json.dump(date,f,indent=4)
print("生成されたセッションID",session_id)


#🔹 安全シミュレーション問題集（10問）

#ローカルサーバ向けの安全なリクエスト/テストユーティリティ集。
#---- 安全注意 ----
#必ず localhost または自分のテストサーバに対してのみ実行してください。
#HTTPリクエスト連打のシミュレーション ローカルサーバーに 10 回だけ GET リクエストを送るコードを書け。ステータスコードを表示せよ。
import requests

url = ""  # ローカルサーバのURLに置き換えてください

for i in range(10):
    try:
        r = requests.get(url)
        print(f"リクエスト{i+1}: ステータスコード {r.status_code}")
    except Exception as e:
        print(f"リクエスト{i+1} 失敗: {e}")
#ループ回数と待機時間の調整 連続リクエストで 1 秒間隔を入れた場合、10 回リクエストでかかる総時間を計算せよ。
import time
import requests
url=""
strt_time=time.time()
for i in range(10):
    try:
        r=requests.get(url)
        print(f"リクエスト{i+1}:ステータスコード{r.status_code}")
        time.sleep(1)
    except Exception as e:
        print(f"リクエスト{i+1}失敗:{e}")
end_time=time.time()
print(f"総合時間:{end_time - strt_time:.2f}秒")
#並列リクエストのシミュレーション threading を使って 3 本のスレッドで同時にリクエストを送る安全なコードを書け。
import threading
import requests
url=""
def send_request(thread_id):
    try:
        r=requests.get(url)
        print(f"スレッド{thread_id}:ステータスコード:{r.status_code}")
    except Exception as e:
        print(f"スレッド{thread_id}失敗:{e}")
threads=[]
for i in range(3):
    t=threading.Thread(target=send_request,args=(i+1,))
    t.start()
    threads.append(t)
    for i in threads:
        t.join()
    print("全て終了")
#ランダムなURLアクセスのシミュレーション ローカルにある /page1、/page2、/page3 にランダムでアクセスするコードを書け。
import random
import requests
urls={
    "http://名前/page1",
    "http://名前/page2",
    "http://名前/page3"
}
for i in range(10):
    url=random.choice(urls)
    try:
        r=requests.get(url)
        print(f"アクセスURL:{url},ステータスコード:{r.status_code}")
    except Exception as e:
        print(f"アクセス失敗:{e}")
#ログの記録 送信したリクエストの時刻とステータスコードを CSV に書き込む安全コードを作れ。
import csv
import requests
import time
url="個人のURL"
with open ("request_log.csv","w",newline="",encoding="utf-8") as f:
    witer=csv.writer(f)
    witer.writerow(["送信時刻","ステータスコード"])
    for i in range(10):
        try:
            r=requests.get(url)
            current_time=time.strftime("%Y-$m-$d %H:%M:$S")
            witer.writerow([current_time,r.status_code])
            print(f"アクセスURl:{urls},ステータスコード:{r.status_code}")
        except Exception as e:
            print(f"アクセスURL:{url}失敗:{e}")
#リクエスト回数制限チェック 1 秒に 2 回以上リクエストを送るとエラーを出す制御を追加せよ。
import time
import requests

url = ""  # ローカルサーバーに置き換え
last_request_time = 0
min_interval = 0.5  # 1秒に2回まで

for i in range(10):
    current_time = time.time()
    if current_time - last_request_time < min_interval:
        wait_time = min_interval - (current_time - last_request_time)
        print(f"リクエストが多すぎます。{wait_time:.2f}秒待機します。")
        time.sleep(wait_time)
    
    try:
        r = requests.get(url)
        print(f"アクセスURL: {url}, ステータスコード: {r.status_code}")
        last_request_time = time.time()
    except Exception as e:
        print(f"アクセスURL: {url} 失敗: {e}")

#応答時間測定 リクエストを送った際の応答時間を計測して平均値を表示せよ。
import requests
import time

url = ""  # ローカルサーバーに置き換え
request_times = []

for i in range(10):
    start_time = time.time()
    try:
        r = requests.get(url)
        end_time = time.time()
        elapsed = end_time - start_time
        request_times.append(elapsed)
        print(f"アクセスURL: {url}, ステータスコード: {r.status_code}, 応答時間: {elapsed:.3f}秒")
    except Exception as e:
        print(f"アクセスURL: {url} 失敗: {e}")

if request_times:
    avg_time = sum(request_times) / len(request_times)
    print(f"平均応答時間: {avg_time:.3f}秒")

#フォーム送信の安全シミュレーション ローカルのテストフォームに POST でデータを送信するコードを書け。
import requests

url = ""  # ローカルのテストフォームURL
data = {"name": "test", "age": 30}

try:
    r = requests.post(url, data=data)
    print(f"アクセスURL: {url}, ステータスコード: {r.status_code}")
except Exception as e:
    print(f"アクセスURL: {url} 失敗: {e}")
#攻撃パターンの再現 GET、POST を交互に 5 回ずつ送信する安全なコードを書け。
import requests

url = ""  # ローカルサーバーに置き換え

for i in range(10):
    try:
        if i % 2 == 0:
            r = requests.get(url)
            method = "GET"
        else:
            r = requests.post(url, data={"key": "value"})
            method = "POST"
        print(f"リクエスト{i+1}: メソッド {method}, アクセスURL: {url}, ステータスコード: {r.status_code}")
    except Exception as e:
        print(f"リクエスト{i+1} 失敗: {e}")

#異常値のテスト URL が間違っていた場合の例外処理を追加して、エラーをログに残すコードを書け。
import requests
import logging

url = ""  # テスト用に間違ったURL

# ログ設定
logging.basicConfig(filename="error.log", filemode="a", level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

try:
    r = requests.get(url)
    print(f"アクセスURL: {url}, ステータスコード: {r.status_code}")
except Exception as e:
    logging.error(f"リクエスト失敗: {e}")
    print(f"アクセスURL: {url} 失敗: {e}")


# 1. 文字列 "Hello, World!" を逆順に表示せよ。
s="hello"+"World!"
s=s[::-1]
print(s)
# 2. "python" を大文字に変換せよ。
s="python"
print(s.upper())
# 3. "Python" を小文字に変換せよ。
s="python"
s.istitle()
print(s.lower())
# 4. "Hello123" から数字だけを抽出せよ。
import re
math="Hello123"
result=re.sub(r"\D","",math)
print(result)
# 5. "a,b,c,d" をリスト ['a','b','c','d'] に変換せよ。
list_post="a,b,c,d"
result=list_post.split(",")
print(result)
# 6. リスト ['a','b','c'] を "abc" に結合せよ。
list_post=['a','b','c']
result="".json(list_post)
print(result)
# 7. "hello world" の先頭文字を "H" に置換せよ。
S="hello world"
result=s.replace("h","H",1)
print(result)
# 8. Base64で "PythonCTF" をエンコードせよ。
import base64
s="PythonCTF"
encode=base64.b64encode(s.encode())
print(encode)
# 9. Base64をデコードして元に戻せ。
decode=base64.b64decode(encode).decode()
print(decode)
# 10. URLエンコードして文字列 "a b+c" を変換せよ。
import urllib.parse
s="a b+c"
url_encode=urllib.parse.quote(s)
print(url_encode)
# 11. URLデコードして元に戻せ。
url_decode=urllib.parse.unquote(url_encode)
print(url_decode)
# 12. 文字列 "level" が回文か判定せよ。
s="level"
if s==s[::-1]:
    print("回文です")
# 13. "listen" と "silent" がアナグラムか判定せよ。
s1="listen"
s2="silent"
if sorted(s1)==sorted(s2):
    print("アナグラムです")
# 14. Caesar暗号で "abc" を3シフトして暗号化せよ。
def caesar_cipher(text,shift):
    result=""
    for char in text:
        if char.isalpha():
            shift_base=ord('a') if char.isalowrr() else ord('A')
            shifted_char=chr((ord(char)-shift_base+shift)%26 +shift_base)
            result+=shifted_char
        else:
            result+=char
        return result
encrypted=caesar_cipher("abc",3)
print(encrypted)
# 15. Caesar暗号を復号して元に戻せ。
decrypted=caesar_cipher("def",-3)
print(decrypted)
# 16. XOR暗号で文字列 "hello" を暗号化せよ（キー1文字）。
def xor_cipher(text,key):
    result=""
    for char in text:
        result+=chr(ord(char)^ord(key))
    return result
encrypted=xor_cipher("hello","K")
print(encrypted)
# 17. XOR暗号を復号して元に戻せ。
decrypted=xor_cipher(encrypted,"K")
print(decrypted)
# 18. 文字列をASCIIコードのリストに変換して出力せよ。
s="hello"
ascii_list=[ord(char) for char in s]
print(ascii_list)
# 19. ASCIIコードのリストから文字列に戻せ。
chars=[104,101,108,108,111]
result="".join(chr(code) for code in chars)
print(result)
# 20. 文字列の各文字の出現回数を辞書で数えよ。
s="hello world"
char_count={}
for char in s:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1
    print(char_count)
    
# ===== 21〜40: ハッシュ・暗号系 =====
import hashlib
import json
import secrets
import uuid
import re
import itertools
import string
import os
import html

s = "password"

# 21. SHA-256
hash_hex = hashlib.sha256(s.encode()).hexdigest()
print("SHA-256:", hash_hex)

# 22. SHA-1
hash_hex = hashlib.sha1(s.encode()).hexdigest()
print("SHA-1:", hash_hex)

# 23. MD5
hash_hex = hashlib.md5(s.encode()).hexdigest()
print("MD5:", hash_hex)

# 24. 同じ文字列を2回ハッシュ
hash1 = hashlib.sha256(s.encode()).hexdigest()
hash2 = hashlib.sha256(s.encode()).hexdigest()
print("1回目:", hash1)
print("2回目:", hash2)

# 25. ソルト付きハッシュ
salt = "random_salt"
hash_hex = hashlib.sha256((s + salt).encode()).hexdigest()
print("ソルト付き:", hash_hex)

# 26. ハッシュと平文の一致確認
def verify_hash(hash_value, plain_text):
    return hashlib.sha256(plain_text.encode()).hexdigest() == hash_value
print("一致確認:", verify_hash(hash_hex, "password"))

# 27. 辞書攻撃シミュレーション（安全）
hash_list = ["123", "password", "admin"]
target_hash = hashlib.sha256("password".encode()).hexdigest()
for word in hash_list:
    if hashlib.sha256(word.encode()).hexdigest() == target_hash:
        print("見つかりました:", word)
        break

# 28. ハッシュを辞書に保存
hash_dict = {"password": hashlib.sha256("password".encode()).hexdigest()}
print(hash_dict)

# 29. JSONに保存
with open("hashes.json", "w") as f:
    json.dump(hash_dict, f, indent=4)
    print("保存しました")

# 30. JSONを読み込む
with open("hashes.json", "r") as f:
    load_users = json.load(f)
    print("読み込み:", load_users)

# 31. secrets でセッションID
session_id = secrets.token_urlsafe(16)
print("生成されたセッションID:", session_id)

# 32. uuid
unique_id = uuid.uuid4()
print("生成されたUUID:", unique_id)

# 33. ハッシュ関数
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()
print("mypasswordのハッシュ:", hash_password("mypassword"))

# 34. パスワード強度チェック
def check_password_strength(password: str) -> str:
    if len(password) < 8:
        return "パスワードは8文字以上にしてください"
    if not re.search(r"[A-Z]", password):
        return "大文字が含まれていません"
    if not re.search(r"[a-z]", password):
        return "小文字が含まれていません"
    if not re.search(r"\d", password):
        return "数字が含まれていません"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "記号が含まれていません"
    return "強力なパスワードです"
print(check_password_strength("Abc123!"))

# 35. 総当たりシミュレーション（短い範囲のみ）
target_password = "Ab1!"
target_hash = hashlib.sha256(target_password.encode()).hexdigest()
char = string.ascii_letters + string.digits + "!@#"
for length in range(2, 5):
    for attempt in itertools.product(char, repeat=length):
        attempt_str = ''.join(attempt)
        if hashlib.sha256(attempt_str.encode()).hexdigest() == target_hash:
            print("解読に成功:", attempt_str)
            break

# 36. ランダムソルト
salt = os.urandom(16).hex()
print("生成されたソルト:", salt)

# 37. 辞書とハッシュ比較
def check_password_in_dict(hash_value, password_list):
    for word in password_list:
        if hashlib.sha256(word.encode()).hexdigest() == hash_value:
            return word
    return None
print("辞書で発見:", check_password_in_dict(target_hash, ["123", "password", "admin"]))

# 38. HTMLエスケープ
def sanitize_input(user_input):
    return html.escape(user_input)
user_comment = '<script>alert("危険!")</script>'
safe_comment = sanitize_input(user_comment)
print("元の入力:", user_comment)
print("エスケープ後:", safe_comment)

# 39. 危険文字チェック
def contains_dangerous_chars(user_input):
    danger_chars = [";", "'", "\""]
    return any(char in user_input for char in danger_chars)
print("危険文字チェック:", contains_dangerous_chars("hello world"))

# 40. HTML安全出力（エスケープ＋最小化）
def safe_html_output(user_input):
    escaped_input = html.escape(user_input)
    minimized_input = " ".join(escaped_input.split())
    return minimized_input
print("安全出力:", safe_html_output(' <b> Hello  World </b> '))
# ===== 41~60:　ネットワーク.サイバー系 =====
#41. 自分のPCのホスト名とIPアドレスを取得せよ。
import socket
hostname=socket.gethostname()
try:
    ip_address=socket.gethostbyname(hostname)
except socket.gaierror:
    ip_address="IPアドレスが取得できません"
print("ホスト名:",hostname)
print("IPアドレス:", ip_address)
#42. 特定のホスト（例: example.com）のIPアドレスを取得せよ。
import socket
hostn = "example.com"   # 必要なら別のホストに変更
try:
    ip_addr = socket.gethostbyname(hostn)
    print(f"{hostn} の IPアドレス: {ip_addr}")
except Exception as e:
    print(f"{hostn} のIP取得失敗: {e}")

# 43. HTTPS サイトに安全に接続し、サーバ証明書を表示せよ。
import ssl
import socket
hostname = "example.com"  # 確認したいホストに変更
context = ssl.create_default_context()
try:
    with socket.create_connection((hostname, 443), timeout=5) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            print(f"{hostname} のサーバ証明書:")
            for k, v in cert.items():
                print(f"  {k}: {v}")
except Exception as e:
    print(f"証明書取得失敗: {e}")


# 44. ローカルホストに対して 1〜100 のポートスキャンを行い、開いているポートを表示せよ。
import socket
target_ip = "127.0.0.1"  # ローカルで安全にテスト
start_port = 1
end_port = 100
open_ports = []
for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.2)
    try:
        result = s.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
    except Exception:
        pass
    finally:
        s.close()
print("開いているポート:", open_ports)
print("ポートスキャン終わり")


# 45. HTTPヘッダーを取得して、セキュリティ関連ヘッダーが存在するか確認せよ。
import requests
url = "https://example.com"  # 確認したいURLに変更
try:
    response = requests.get(url, timeout=5)
    security_headers = [
        "Content-Security-Policy",
        "X-Content-Type-Options",
        "X-Frame-Options",
        "Strict-Transport-Security",
        "Referrer-Policy",
        "Permissions-Policy"
    ]
    print("取得したヘッダー:")
    for k, v in response.headers.items():
        print(f"  {k}: {v}")
    print("\nセキュリティ関連ヘッダーの有無:")
    for h in security_headers:
        print(f"  {h}: {'あり' if h in response.headers else 'なし'}")
except Exception as e:
    print(f"HTTPヘッダー取得失敗: {e}")


# 46. URL からドメイン部分だけを抽出せよ。
from urllib.parse import urlparse
url = "https://example.com/login?user=1"
parsed = urlparse(url)
domain = parsed.netloc
print("ドメイン:", domain)


# 47. 疑似的な「Ping」として、特定ホストに TCP 接続できるか確認する関数を作れ。
import socket
def tcp_ping(host, port=80, timeout=1):
    try:
        s = socket.create_connection((host, port), timeout=timeout)
        s.close()
        return True
    except Exception:
        return False

# 使用例
host = "example.com"
port = 80
print(f"{host}:{port} に接続可能か:", tcp_ping(host, port, timeout=2))


# 48. セッションIDをランダム生成し、アクセスログ（IP・時刻・セッションID）を記録せよ。
import secrets
import time
import socket
def write_access_log(client_ip=None):
    # client_ip が None の場合はローカルIP を使う
    if client_ip is None:
        try:
            client_ip = socket.gethostbyname(socket.gethostname())
        except Exception:
            client_ip = "unknown"
    session_id = secrets.token_urlsafe(16)
    access_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log_line = f"{access_time},{client_ip},{session_id}"
    with open("access.log", "a", encoding="utf-8") as f:
        f.write(log_line + "\n")
    print("アクセスログ:", log_line)

# テスト書き込み
write_access_log()


# 49. HTTPS接続で使用している TLS/SSL のバージョンを取得せよ。
import ssl
import socket
hostname = "example.com"
context = ssl.create_default_context()
try:
    with socket.create_connection((hostname, 443), timeout=5) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            tls_version = ssock.version()
            print(f"{hostname} の TLS/SSL バージョン: {tls_version}")
except Exception as e:
    print(f"TLSバージョン取得失敗: {e}")


# 50. メッセージを SHA-256 でハッシュし、改ざん検証できるようにせよ。
import hashlib
def hash_message(message: str) -> str:
    return hashlib.sha256(message.encode()).hexdigest()

message = "重要メッセージ"
hash_value = hash_message(message)
print("メッセージ:", message)
print("SHA-256:", hash_value)

# 改ざん検証の例
def verify_message(message: str, expected_hash: str) -> bool:
    return hash_message(message) == expected_hash

print("検証:", verify_message("重要メッセージ", hash_value))

#通信と検証
# 51. HTTP でアクセスしたとき、HTTPS にリダイレクトされるか確認せよ。
import requests
url = "http://example.com"
try:
    r = requests.get(url, timeout=5)
    if r.url.startswith("https://"):
        print(f"{url} は HTTPS にリダイレクトされました -> {r.url}")
    else:
        print(f"{url} は HTTPS にリダイレクトされませんでした")
except Exception as e:
    print(f"アクセス失敗: {e}")


# 52. Pythonで簡易的なローカルサーバを起動してポートに待ち受けさせよ。
import http.server
import socketserver
PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()


# 53. example.com の DNS 情報を取得して表示せよ。
import socket
hostname = "example.com"
try:
    ip_address = socket.gethostbyname(hostname)
    print(f"{hostname} のIPアドレス: {ip_address}")
except Exception as e:
    print(f"DNS取得失敗: {e}")


# 54. HTTPS サイトのレスポンス本文を SHA-256 でハッシュして検証せよ。
import requests
import hashlib
url = "https://example.com"
try:
    r = requests.get(url, timeout=5)
    body_hash = hashlib.sha256(r.content).hexdigest()
    print(f"{url} のレスポンスSHA-256: {body_hash}")
except Exception as e:
    print(f"アクセス失敗: {e}")


# 55. 複数のURLにアクセスし、それぞれのレスポンスステータスコードを確認せよ。
import requests
urls = []
for i in range(2):  # テスト用に 2 個だけ
    url = input("URL入力: ")
    urls.append(url)

for url in urls:
    try:
        r = requests.get(url, timeout=5)  # ← .grt → .get に修正
        print(f"{url} のステータスコード: {r.status_code}")
    except Exception as e:
        print(f"{url} のアクセス失敗: {e}")


# 56. SSL証明書の有効期限を取得して表示せよ。
import ssl
import socket
hostname = "example.com"
context = ssl.create_default_context()
try:
    with socket.create_connection((hostname, 443), timeout=5) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:  # ← ssok → ssock に修正
            cert = ssock.getpeercert()
            not_after = cert.get("notAfter")
            print(f"{hostname} のSSL証明書の有効期限: {not_after}")
except Exception as e:
    print(f"証明書取得失敗: {e}")


# 57. HTTPSレスポンスの Content-Type を確認せよ。
import requests
url = "https://example.com"
try:
    r = requests.get(url, timeout=5)
    content_type = r.headers.get("Content-Type")  # ← conntent_type → content_type に修正
    print(f"{url} のContent-Type: {content_type}")
except Exception as e:
    print(f"アクセス失敗: {e}")


# 58. 複数のポート（80, 443, 22）に接続を試み、開いているか閉じているかを表示せよ。
import socket
target_ip = "93.184.216.34"  # example.com のIP例
ports = [80, 443, 22]
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
    except Exception as e:
        print(f"Port {port} の接続失敗: {e}")
    finally:
        s.close()


# 59. 通信ログ（URL、ステータスコード、本文のSHA-256）を JSON 形式で保存せよ。
import requests
import hashlib
import json
url = "https://example.com"
log_data = {}
try:
    r = requests.get(url, timeout=5)
    body_hash = hashlib.sha256(r.content).hexdigest()
    log_data = {
        "url": url,
        "status_code": r.status_code,
        "body_sha256": body_hash
    }
    with open("comm_log.json", "w", encoding="utf-8") as f:
        json.dump(log_data, f, indent=4)
        print("通信ログを保存しました")
except Exception as e:
    print(f"アクセス失敗: {e}")


# 60. 保存した通信ログを読み込み、整形して出力せよ。
import json
try:
    with open("comm_log.json", "r", encoding="utf-8") as f:
        log_data = json.load(f)
        print("通信ログ:")
        print(f"URL: {log_data.get('url')}")
        print(f"ステータスコード: {log_data.get('status_code')}")
        print(f"本文のSHA-256: {log_data.get('body_sha256')}")
except Exception as e:
    print(f"ログの読みとり失敗: {e}")

# 51. Caesar暗号で「HELLO」を3文字シフトした暗号文を求めよ。
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += shifted_char
        else:
            result += char
    return result

encrypted = caesar_cipher("HELLO", 3)
print("Caesar暗号(HELLO, +3):", encrypted)

# 52. Caesar暗号「KHOOR」を復号せよ。
decrypted = caesar_cipher("KHOOR", -3)
print("Caesar復号(KHOOR, -3):", decrypted)


# 53. ROT13で「python」を暗号化
import codecs
text = "python"
rot13_text = codecs.encode(text, "rot_13")
print("ROT13暗号(python):", rot13_text)

# 54. ROT13で「clguba」を復号
cipher_text = "clguba"
decoded_txt = codecs.decode(cipher_text, "rot_13")
print("ROT13復号(clguba):", decoded_txt)


# 55. Atbash暗号（A↔Z, B↔Y …）
def atbash_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            atbash_char = chr(shift_base + (25 - (ord(char) - shift_base)))
            result += atbash_char
        else:
            result += char
    return result

encrypted = atbash_cipher("CTF")
print("Atbash暗号(CTF):", encrypted)

decrypted = atbash_cipher("XUG")
print("Atbash復号(XUG):", decrypted)


# 56. Vigenère暗号
def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[i % key_length]) - ord('A')
            value = (ord(char) - shift_base + shift) % 26
            result += chr(value + shift_base)
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ""
    key = key.upper()
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[i % key_length]) - ord('A')
            value = (ord(char) - shift_base - shift) % 26
            result += chr(value + shift_base)
        else:
            result += char
    return result

encrypted = vigenere_encrypt("ATTACK", "KEY")
print("Vigenere暗号(ATTACK, KEY):", encrypted)

decrypted = vigenere_decrypt("KXRZVI", "KEY")
print("Vigenere復号(KXRZVI, KEY):", decrypted)


# 57. シンプル置換暗号 (A→Z, B→Y…)
# → これは Atbash と同じ
decrypted_int = atbash_cipher("FLAG")
print("置換暗号(FLAG):", decrypted_int)

decrypted = atbash_cipher("UOZT")
print("置換復号(UOZT):", decrypted)

# 文字列「password」をMD5でハッシュ化
import hashlib
s = "password"
hash_md5 = hashlib.md5(s.encode()).hexdigest()
print("MD5:", hash_md5)


# 文字列「ctf123」をSHA1でハッシュ化
s = "ctf123"
hash_sha1 = hashlib.sha1(s.encode()).hexdigest()
print("SHA1:", hash_sha1)


# 文字列「HELLO」をSHA256でハッシュ化
s = "HELLO"
hash_sha256 = hashlib.sha256(s.encode()).hexdigest()
print("SHA256:", hash_sha256)


# 与えられたMD5ハッシュが表す平文を探す
target_hash = "5f4dcc3b5aa765d61d8327deb882cf99"
word_list = ["123456", "password", "letmein", "qwerty", "abc123"]
for word in word_list:
    if hashlib.md5(word.encode()).hexdigest() == target_hash:
        print("見つかりました:", word)
        break


# 与えられたSHA256ハッシュが表す平文を探す
target_hash = "2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"
word_list = ["foo", "bar", "baz", "hello", "world"]
for word in word_list:
    if hashlib.sha256(word.encode()).hexdigest() == target_hash:
        print("見つかりました:", word)
        break


# 文字列「CTF」をBase64でエンコード
import base64
s = "CTF"
encoded = base64.b64encode(s.encode()).decode()
print("Base64エンコード:", encoded)


# Base64文字列「UHl0aG9u」をデコード
s = "UHl0aG9u"  # ← typo修正
decoded = base64.b64decode(s).decode()
print("Base64デコード:", decoded)


# URLエンコードで「flag=123」を変換
import urllib.parse
s = "flag=123"
url_encode = urllib.parse.quote(s)
print("URLエンコード:", url_encode)


# URLデコードで「ZmxhZyUzRDEyMw%3D%3D」を復号
s = "ZmxhZyUzRDEyMw%3D%3D"
url_decode = urllib.parse.unquote(s)
print("URLデコード:", url_decode)


# Hex文字列「666c6167」をASCII文字列に変換
import binascii
hex_str = "666c6167"
ascii_str = binascii.unhexlify(hex_str).decode()
print("Hex→ASCII:", ascii_str)

