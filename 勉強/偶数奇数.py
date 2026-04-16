数字 = int(input("数字を入力してください"))
if 数字 % 2 == 0:
    print("even")
else:
    print("odd")
    
#2) 1〜100の合計
for sum in range(1,101):
    print(sum)

#リストの最大値
numbers = [5, 2, 10, 7, 1]
numbers_max = max(numbers)
print(numbers_max)

#4) 文字数カウント
文字列 = "security"
print(len(文字列))

#FizzBuzz（超重要）
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#パスワード簡易チェック
password = input("password: ")

if len(password) >= 8:
    print("OK")
else:
    print("NG")
    
#7) 辞書でユーザー情報
user = {"name": "John", "age": 25}
name = user["name"]
print(name)

#8) ファイル保存
memo = ["jun"]
with open("memo.txt","w",encoding="UTF-8") as f:
    for line in memo:
        f.write(line+"\n")

#9) 簡単な関数
def add(a,b):
    c = a + b
    print(c)
add(1,3)
#10) エラーハンドリング
try:
    x = 10 / 0
except ZeroDivisionError:
    print("0で割ったらエラーにならないようにする")

#APIからJSONを取得して処理する
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
data = requests.json()

for user in data:
    print(user["name"])

