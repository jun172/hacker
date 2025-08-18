X# -----------------------------
# 1. 1〜50までの素数をリスト化
# -----------------------------
primes = [n for n in range(2, 51) if all(n % i != 0 for i in range(2, n))]
print("素数:", primes)


# -----------------------------
# 2. フィボナッチ数列を20個生成
# -----------------------------
fib = [0, 1]
for _ in range(18):
    fib.append(fib[-1] + fib[-2])
print("フィボナッチ:", fib)


# -----------------------------
# 3. ユーザーに数値入力 → 階乗を計算
# -----------------------------
n = int(input("数値を入力: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"{n} の階乗:", fact)


# -----------------------------
# 4. CSVファイルから「年齢30以上」の行を抽出
# -----------------------------
import csv
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if int(row[1]) >= 30:   # 年齢が2列目にある場合
            print(row)


# -----------------------------
# 5. リスト [2,4,6,8,10] の平均値を求める
# -----------------------------
nums = [2, 4, 6, 8, 10]
avg = sum(nums) / len(nums)
print("平均値:", avg)


# -----------------------------
# 6. 与えられた文字列の母音数を数える
# -----------------------------
s = "example"
vowels = sum(1 for c in s if c.lower() in "aeiou")
print("母音の数:", vowels)


# -----------------------------
# 7. リスト [1,2,3] と [4,5,6] を結合
# -----------------------------
a = [1,2,3]
b = [4,5,6]
c = a + b
print("結合リスト:", c)


# -----------------------------
# 8. 文字列 "abracadabra" の 'a' の出現回数
# -----------------------------
s = "abracadabra"
count_a = s.count('a')
print("'a' の出現回数:", count_a)


# -----------------------------
# 9. 入力文字列が回文か判定
# -----------------------------
s = input("文字列を入力: ")
if s == s[::-1]:
    print("回文です")
else:
    print("回文ではありません")


# -----------------------------
# 10. リスト [3,5,7,9] の各要素を2乗した新リスト作成
# -----------------------------
nums = [3,5,7,9]
squared = [x**2 for x in nums]
print("2乗リスト:", squared)


# -----------------------------
# 11. タプル (10,20,30) の合計を求める
# -----------------------------
t = (10,20,30)
print("合計:", sum(t))


# -----------------------------
# 12. JSONファイルから "username" の値を取り出す
# -----------------------------
import json
with open('sample.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
print("username:", data.get("username"))


# -----------------------------
# 13. ランダムに英数字8文字のパスワードを生成
# -----------------------------
import random, string
chars = string.ascii_letters + string.digits
password = "".join(random.choice(chars) for _ in range(8))
print("生成パスワード:", password)


# -----------------------------
# 14. APIレスポンス(JSON)をパースして値抽出
# -----------------------------
response = '{"key": 123, "name": "Alice"}'
data = json.loads(response)
print("keyの値:", data.get("key"))


# -----------------------------
# 15. 簡易Todoリスト CLI（追加・削除・一覧表示）
# -----------------------------
todo = []
while True:
    action = input("追加(a)/削除(d)/一覧(l)/終了(q): ").lower()
    if action == 'a':
        task = input("追加するタスク: ")
        todo.append(task)
        print(f"追加しました: {task}")
    elif action == 'd':
        task = input("削除するタスク: ")
        if task in todo:
            todo.remove(task)
            print(f"削除しました: {task}")
        else:
            print("タスクが見つかりません")
    elif action == 'l':
        print("Todoリスト:")
        for t in todo:
            print("-", t)
    elif action == 'q':
        print("終了します")
        break
    else:
        print("無効な入力です")
