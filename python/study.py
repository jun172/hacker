a = 10
b = "20"
print(a+int(b))

x = int(input("数字を入力してください: "))

if x % 2 == 0:
    print("偶数")
else:
    print("奇数")
    
for x in range(1, 21):
    if x % 3 == 0:
        print(x)
        
def add(x, y):
    return x + y

result = add(5, 7)
print(result)

def add(x, y):
    return x + y

result = add(5, 7)
print(result)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"私は{self.name}です。年齢は{self.age}歳です。")

p1 = Person("John", 25)
p1.greet()

import datetime
import random
import json

# 日付
dt_time = datetime.datetime.now()
print(dt_time)

# ランダム
random_number = random.randint(1, 100)
print(random_number)

# JSON変換
data = {"name": "Alice", "age": 25}
json_string = json.dumps(data)
print(json_string)

#書き込み
with open("numbers.txt","w") as f:
    for i in range(1,6):
        f.write(str(i) + "\n")

#読み込み
total = 0
with open("numbers.txt","r") as f:
    for line in f:
        total += int(line.strip())
    
print("合計",total)

import sqlite3

conn = sqlite3.connect("test.db")
corsor = conn.cursor()

corsor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER KEY, name TEXT)")
corsor.execute("INSERT INTO user (name) VALUES (?)",("Alice",))

conn.commit()

corsor.execute("SELECT * FROM users")
rows = corsor.fetchall()

for row in rows:
    print(row)

conn.close()

#ミッション1：return完全理解
def sum_even(numbers):
    total = 0 #合計用変数を作る
    for num in numbers: #リストをループ
        if num % 2 == 0: #偶数判定
            total += num #合計に加算
    return total #最後にreturn
#ミッション2：クラス理解
class BankAccount:
    def __init__(self,owner,balance): #コンストラクタ（init）
        self.owner = owner
        self.balance += balance
        
    def deposit(self,amount):
        self.balance += amount
        print(f"{amount}円引き出しました。")
        
    def withdraw(self,amount):
        if amount > self.balance:
            print("残高不足")
        else:
            self.balance -= amount
            print(f"{amount}円引き出しました。")
            
    def show_balance(self):
        print(f"現在の残高は{self.balance}円です。")

account = BankAccount("John",1000)

account.show_balance()
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)
account.show_balance()

#ミッション3：jsonとファイル操作
import json
#① データ作成
data = {"name":"John","age":30}

#② JSONファイルに保存
with open("user.json","w") as f:
    json.dump(data,f)

#③ JSONファイルを読み込み
with open("user.json","r") as f:
    loaded_data = json.load(f)
    
#④ nameだけ表示
print(loaded_data["name"])

