# =====================================
# 1. IPアドレス抽出
# =====================================

import re  # 正規表現モジュールを読み込む

ip_list = []  # 抽出したIPアドレスを入れる空リストを作成

# server.log ファイルを読み込み
with open("server.log", "r", encoding="utf-8") as f:
    for line in f:  # ファイルを1行ずつ処理
        # 正規表現でIPv4形式のIPを探す
        ips = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", line)
        # 見つかったIPをリストに追加
        ip_list.extend(ips)

# 重複を除いてIPを表示
print("抽出されたIP:")
for ip in set(ip_list):
    print(ip)

# 💡アドバイス：
# IPの範囲チェック（0-255）までは正規表現では厳密にできていません。
# 実務では ipaddress モジュールを使うと安全です。


# =====================================
# 2. 辞書の値の平均
# =====================================

mylist = { "Alice": [80, 90, 100], "Bob": [70, 85, 90] }

# 各人の平均点を計算
for name, scores in mylist.items():
    avg = sum(scores) / len(scores)  # 平均 = 合計 ÷ 個数
    print(f"{name} の平均点: {avg}")

# 💡修正ポイント：
# 元のコードでは `sum(mylist)/len(mylist)` としていましたが
# 辞書は直接 sum できないので、各値（リスト）を対象に計算する必要があります。


# =====================================
# 3. 単語出現ランキング
# =====================================

from collections import Counter  # 単語の出現回数を数えるために使用

with open("words.txt", "r", encoding="utf-8") as f:
    text = f.read()  # ファイル全体を読み込み

words = text.split()  # 空白で単語に分割

counter = Counter(words)  # 出現回数をカウント

top5 = counter.most_common(5)  # 出現回数上位5単語を取得

print("単語出現ランキングTOP5:")
for word, count in top5:
    print(f"{word}: {count}回")

# 💡修正ポイント：
# 元のコードでは `text.split` の後ろに `()` が抜けていた。
# また `Counter.most_common(5)` は counter インスタンスから呼び出す必要があります。


# =====================================
# 4. ポート番号判定
# =====================================

port = int(input("ポート番号を入力してください: "))  # ユーザーから整数を入力

if port == 22:
    print("SSH")
elif port == 80:
    print("HTTP")
elif port == 443:
    print("HTTPS")
else:
    print("不明なポート")

# 💡アドバイス：
# よく使うポート番号を辞書で管理しても便利です。
# 例: ports = {22:"SSH", 80:"HTTP", 443:"HTTPS"}


# =====================================
# 5. JSONファイル読み込み
# =====================================

import json  # JSON操作用モジュール

with open("users.json", "r", encoding="utf-8") as f:
    data = json.load(f)  # JSONファイルをPythonのデータ型に変換

print("JSON内容:")
print(data)

# 💡修正ポイント：
# 元のコードでは `json=[]` としてしまい、jsonモジュールを上書きしていた。
# 必ず別の変数名にして読み込むこと。


# コメントアウト開始
# │
# ├─▶ 1. IPアドレス抽出
# │       │
# │       ├─ open("server.log")
# │       │
# │       ├─ 1行ずつ読み込み
# │       │
# │       ├─ 正規表現でIPを抽出
# │       │
# │       ├─ ip_list に追加
# │       │
# │       └─ set(ip_list) を表示
# │
# ├─▶ 2. 辞書の平均点計算
# │       │
# │       ├─ mylist = {"Alice":[...], "Bob":[...]}
# │       │
# │       ├─ 各人のスコアを sum/len で平均計算
# │       │
# │       └─ 名前と平均点を表示
# │
# ├─▶ 3. 単語出現ランキング
# │       │
# │       ├─ open("words.txt") で読み込み
# │       │
# │       ├─ text.split() で単語リスト作成
# │       │
# │       ├─ Counter で出現回数カウント
# │       │
# │       └─ 上位5単語を表示
# │
# ├─▶ 4. ポート番号判定
# │       │
# │       ├─ port = int(input())
# │       │
# │       ├─ port==22 ? → "SSH"
# │       │
# │       ├─ port==80 ? → "HTTP"
# │       │
# │       ├─ port==443 ? → "HTTPS"
# │       │
# │       └─ else → "不明なポート"
# │
# ├─▶ 5. JSONファイル読み込み
# │       │
# │       ├─ open("users.json")
# │       │
# │       ├─ json.load() でデータ読み込み
# │       │
# │       └─ データ表示
# │
# └─▶ 終了
