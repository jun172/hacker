# 問題1：2つの整数の合計
a = int(input("1つ目の整数: "))
b = int(input("2つ目の整数: "))
print(a + b)


# 問題2：名前を入力して挨拶
text = input("名前を入力: ")
print(f"こんにちは、{text}さん")


# 問題3：三角形の面積
teihen = int(input("底辺: "))
height = int(input("高さ: "))
area = teihen * height / 2
print(area)


# 問題5：年齢判定
age = int(input("年齢: "))
if age >= 18:
    print("いける")
else:
    print("いけない")


# 問題6：偶数・奇数判定
tx = int(input("整数判定: "))
if tx % 2 == 0:
    print("偶数")
else:
    print("奇数")


# 問題7：点数判定
score = int(input("点数: "))
if score >= 80:
    print("A")
elif score >= 60:
    print("B")
elif score >= 40:
    print("C")
else:
    print("D")


# 問題8：ログイン判定
correct_id = "admin"
correct_pw = "1234"

user_id = input("ID: ")
user_pw = input("PW: ")

if user_id == correct_id and user_pw == correct_pw:
    print("成功")
else:
    print("失敗")


# 問題9：1〜10表示
for i in range(1, 11):
    print(i)


# 問題10：1〜100の合計
total = 0
for i in range(1, 101):
    total += i
print(total)

count = int(input("数字:"))
i =0

while i <count:
    print("hello")
    i +=1
    

de =int(input("数字"))
t =0
while t < de:
    print("hello")
    t += 1

count =0
score = int(input("数字"))
count += 1
print(count)

count =int(input("数字を入力:"))
i =0
while i < count:
    print("hello")
    i += 1
    
num =int(input("数字を入力"))
if num % 2 == 0:
    print("偶数")
else:
    print("奇数")


score = int(input("点数を入力"))

if score >= 80:
    print("A")
elif score >= 60:
    print("B")
elif score >= 40:
    print("C")
else:
    print("D")

suzi = int(input("ゼロか非ゼロ"))
if suzi >= 0:
    print("ゼロ")
else:
    print("")