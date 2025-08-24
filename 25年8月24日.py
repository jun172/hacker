# socket
import socket
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print("Hostname:", hostname, "IP:", ip)

# hashlib
import hashlib
hs = hashlib.sha256(b"djeuc")
print("SHA-256:", hs.hexdigest())

# random
import random
letters = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(5))
print("Random letters:", letters)

# datetime
import datetime
today = datetime.date.today()
future = today + datetime.timedelta(days=7)
print("7日後:", future)

# os
import os
print("現在のディレクトリのファイル数:", len(os.listdir(".")))

# itertools
import itertools
ABC = ['A','B','C']
combi = list(itertools.combinations(ABC, 2))
print("組み合わせ:", combi)

# json
import json
data = {"x":10,"y":20}
with open("zisilyo.json","w",encoding="utf-8") as f:
    json.dump(data, f)

# time
import time
start = time.time()
time.sleep(0.5)
print("処理時間:", time.time()-start)

# numpy
import numpy as np
arr = np.arange(1,51)
odds = arr[arr % 2 == 1]
print("奇数:", odds)

# pandas
import pandas as pd
df = pd.DataFrame({"A":[1,2,3], "B":[4,5,6]})
print("平均:", df["A"].mean())

# 1. 1~100か判定
num = int(input("数字: "))
if 1 <= num <= 100:
    print("範囲内")

# 2. 英数字判定
s = input("文字列: ")
if s.isalnum():
    print("英数字のみ")

# 3. リスト内判定
words = ["hello","world"]
if "hello" in words:
    print("含まれる")

# 4. 10の倍数
n = int(input("数: "))
if n % 10 == 0:
    print("10の倍数")

# 5. 大文字/小文字判定
txt = input("文字列: ")
if txt.isupper():
    print("大文字")
elif txt.islower():
    print("小文字")
else:
    print("混在")

# 6. 点数評価
score = int(input("点数: "))
if score >= 80:
    print("優")
elif score >= 60:
    print("良")
elif score >= 40:
    print("可")
else:
    print("不可")

# 7. 三項演算子
num = int(input("整数: "))
print("偶数" if num % 2 == 0 else "奇数")

# 8. all()
lst = [1,2,3]
if all(x>0 for x in lst):
    print("全部正")

# 9. 文字列長さ
txt = input("文字列: ")
if len(txt) < 10:
    print("短い")
elif len(txt) < 30:
    print("普通")
else:
    print("長い")

# 10. match
day = input("曜日 (Mon/Tue...): ")
if day == "Mon":
    print("月曜")
elif day == "Tue":
    print("火曜")
else:
    print("その他")

# len
print(len("hello"))

# sum
nums = [2,4,6]
print(sum(nums))

# max
words = ["apple","mikan","yamada"]
print(max(words))

# min
nums = [-5, 3, 9]
print(min(nums))

# sorted
names = ("sato","suzuki","takahashi")
print(sorted(names))

# zip
a=[1,2,3]
b=[4,5,6]
print(list(zip(a,b)))

# map
nums = [1,2,3]
print(list(map(lambda x:x**2, nums)))

# filter
nums = [-3,5,-7,9]
print(list(filter(lambda x:x<0, nums)))

# any
print(any([0,0,1]))   # True

# all
print(all([2%2==0,4%2==0]))  # True
