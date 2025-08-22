# 1: math
"""
┌───────┐
│ 開始   │
└───┬───┘
    ▼
┌────────────┐
│ math を import │
└─────┬──────┘
      ▼
┌────────────┐
│ 円周率を取得 │
└─────┬──────┘
      ▼
┌────────────┐
│ 結果を出力 │
└─────┬──────┘
      ▼
┌───────┐
│ 終了   │
└───────┘
"""
import math 
print("円周率:", math.pi)


# 2: random
"""
開始 → random を import → リストを作成 → ランダム要素選択 → 出力 → 終了
"""
import random
li = list(range(10))
print("ランダムな要素:", random.choice(li))


# 3: datetime
"""
開始 → datetime を import → 今日の日付取得 → 出力 → 終了
"""
import datetime
today = datetime.date.today()
print("今日の日付:", today)


# 4: os
"""
開始 → os を import → 作業ディレクトリ取得 → 出力 → 終了
"""
import os 
print("現在の作業ディレクトリ:", os.getcwd())


# 5: sys
"""
開始 → sys を import → Pythonバージョン取得 → 出力 → 終了
"""
import sys
print("Pythonのバージョン:", sys.version)


# 6: collections.Counter
"""
開始 → Counter を import → 文字列をカウント → 出力 → 終了
"""
from collections import Counter
kari = Counter("python programming")
print("文字のカウント:", kari)


# 7: statistics
"""
開始 → statistics を import → 平均値計算 → 出力 → 終了
"""
import statistics
kaeru = [10, 20, 30, 40, 50]
print("平均:", statistics.mean(kaeru))


# 8: json
"""
開始 → json を import → 辞書をJSON化 → 出力 → 終了
"""
import json
kerint = {"name":"John","age":25}
print("JSON形式:", json.dumps(kerint, ensure_ascii=False))


# 9: itertools
"""
開始 → itertools を import → 順列を生成 → 出力 → 終了
"""
import itertools
rekai = list(itertools.permutations([1, 2, 3]))
print("全ての順列:", rekai)


# 10: time
"""
開始 → time を import → 時刻を記録 → 1秒待機 → 経過時間を出力 → 終了
"""
import time
start_time = time.time()
time.sleep(1)
print("1秒待ち:", time.time() - start_time, "秒経過")


# 11: numpy
"""
開始 → numpy を import → 配列作成 → 平均計算 → 出力 → 終了
"""
import numpy as np
arry = np.arange(1, 101)
ake = np.mean(arry)
print("平均:", ake)


# 12: pandas
"""
開始 → pandas を import → DataFrame作成 → 欠損値削除 → 出力 → 終了
"""
import pandas as pd
df = pd.DataFrame({"X":[1,2,None,4], "Y":[5,6,7,None]})
df = df.dropna()
print("欠損値削除後:\n", df)


# 13: matplotlib
"""
開始 → matplotlib を import → x,yデータ作成 → 散布図を描画 → 表示 → 終了
"""
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [5,4,3,2,1]
plt.scatter(x, y)
plt.title("散布図")
plt.xlabel("x軸")
plt.ylabel("y軸")
plt.show()


# 14: seaborn
"""
開始 → seaborn を import → データセット読込 → ペアプロット描画 → 表示 → 終了
"""
import seaborn as sns 
iris = sns.load_dataset("iris")
sns.pairplot(iris)
plt.show()


# 15: scikit-learn
"""
開始 → scikit-learn を import → 線形回帰モデル作成 → 学習 → 予測 → 出力 → 終了
"""
from sklearn.linear_model import LinearRegression
X = [[1],[2],[3],[4]]
y = [2,4,6,8]
X_new = [[5]]
model = LinearRegression()
model.fit(X, y)
predictions = model.predict(X_new)
print("予測値:", predictions)


# 16: scipy
"""
開始 → scipy を import → 正規分布サンプル生成 → 出力 → 終了
"""
from scipy.stats import norm
random_numbers = norm.rvs(size=10)
print("正規分布サンプル:", random_numbers)


# 17: hashlib
"""
開始 → hashlib を import → SHA256ハッシュ生成 → 出力 → 終了
"""
import hashlib
m = hashlib.sha256(b"security")
print("SHA256ハッシュ:", m.hexdigest())


# 18: socket
"""
開始 → socket を import → ホスト名取得 → IPアドレス取得 → 出力 → 終了
"""
import socket
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print("ホスト名:", hostname)
print("IPアドレス:", ip_address)


# 19: argparse（スクリプト実行時に有効）
"""
開始 → argparse を import → 引数定義 → 引数解析 → 出力 → 終了
"""
# import argparse
# parser = argparse.ArgumentParser(description="コマンドライン引数の例")
# parser.add_argument("--name", type=str, help="名前を入力してください")
# args = parser.parse_args()
# print("入力された名前:", args.name)


# 20: logging
"""
開始 → logging を import → ログ設定 → INFO出力 → WARNING出力 → ERROR出力 → 終了
"""
import logging
logging.basicConfig(level=logging.INFO)
logging.info("処理開始")
logging.warning("注意")
logging.error("エラー発生")


#実務寄り（セキュリティ・機械学習・Web）
# 21: requests
# HTTP通信でWeb APIからデータ取得
import requests
url = "https://jsonplaceholder.typicode.com/posts"
r = requests.get(url)
print("HTTPステータスコード:", r.status_code)
# → GETリクエストでデータを取得し、ステータスコード(200など)を確認

# 22: BeautifulSoup
# HTML解析
from bs4 import BeautifulSoup
html_doc = "<html><head><title>Test</title></head></html>"
soup = BeautifulSoup(html_doc, 'html.parser')
print("タイトル:", soup.title.string)
# → HTML文書から<title>の中身を抽出

# 23: scapy（実行注意：LAN内スキャンなどは法律違反になる可能性がある）
# LANスキャンの学習例（実行不可）
from scapy.all import ARP, Ether, srp

# スキャン対象ネットワーク（家庭LAN例: 192.168.1.0/24）
target_ip = "192.168.1.0/24"

# ARPリクエストパケット作成
arp = ARP(pdst=target_ip)#ターゲットIPを指定
ether = Ether(dst="ff:ff:ff:ff:ff:ff")#ブロードキャスト送信
packet = ether/arp#送信＆応答受信

# パケット送信・応答取得（タイムアウト2秒）
result = srp(packet, timeout=2, verbose=0)[0]

# 応答があったIPアドレス一覧表示
print("応答のあったIPアドレス一覧:")
for sent, received in result:
    print(f"IP: {received.psrc}, MAC: {received.hwsrc}")
# → パケット操作のライブラリ。ネットワーク学習用。


# 24: cryptography
# 暗号化・復号
from cryptography.fernet import Fernet
key = Fernet.generate_key()  # 秘密鍵生成
cipher = Fernet(key)
plaintext = b"secret message"
ciphertext = cipher.encrypt(plaintext)
print("暗号化されたメッセージ:", ciphertext)
# → AES系暗号でメッセージを安全に暗号化

# 25: sqlite3
# SQLiteでデータベース操作
import sqlite3
db = sqlite3.connect("sample.db")
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
cursor.execute('INSERT INTO persons(name) VALUES (?)', ("taro",))
db.commit()
cursor.execute('SELECT * FROM persons')
rows = cursor.fetchall()
print("テーブル内容:", rows)
db.close()
# → ローカルDBにテーブル作成・データ追加・取得

# 26: flask（簡易Webフォーム受け取り）
from flask import Flask, request, render_template_string
app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f"Hello, {name}!"

# → フォームからPOSTでデータを受け取り画面に表示

# 27: plotly
# インタラクティブグラフ作成
import plotly.express as px
x = ['1','2','3']
y = [50,20,30]
fig = px.bar(x=x, y=y, title='sample bar chart')
fig.show()
# → HTMLで動くインタラクティブ棒グラフを描画

# 28: sklearn cross_val_score
# 交差検証
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data, iris.target
model = LogisticRegression(max_iter=200)
scores = cross_val_score(model, X, y, cv=5)
print("交差検証スコア:", scores)
# → モデルを5分割して精度を評価

# 29: pycryptodome
# AES暗号化と復号
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
plaintext = b"This is a secret message"
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

decipher = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted_plaintext = decipher.decrypt_and_verify(ciphertext, tag)
print("復号結果:", decrypted_plaintext.decode())
# → AES暗号でデータを安全に暗号化・復号

# 30: paramiko（SSH接続・学習用）
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="example.com", username="user", password="pass")
stdin, stdout, stderr = ssh.exec_command("ls")
print(stdout.read().decode())
ssh.close()
# → リモートサーバにSSH接続しコマンド実行（学習用、実運用は注意）

# ┌────────────┐
# │  開始      │
# └─────┬──────┘
#       │
#       ▼
# ┌────────────┐
# │ モジュールを import │
# └─────┬──────┘
#       │
#       ▼
# ┌────────────┐
# │ データ取得・入力 │ (requests, Flask, HTML)
# └─────┬──────┘
#       │
#       ▼
# ┌────────────┐
# │ 処理 │ (暗号化, DB, 機械学習)
# └─────┬──────┘
#       │
#       ▼
# ┌────────────┐
# │ 結果出力 │ (print, plotly, matplotlib)
# └─────┬──────┘
#       │
#       ▼
# ┌────────────┐
# │ 終了      │
# └────────────┘
