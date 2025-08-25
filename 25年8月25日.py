# ───────── ① 入力した数が正か負か ─────────
# 開始
#   ↓
# 入力: num
#   ↓
# num > 0 ?
#   ├─ Yes → 「正の数」
#   └─ No
#       ↓
#       num < 0 ?
#         ├─ Yes → 「負の数」
#         └─ No → 「ゼロ」
num = int(input("数を入力: "))
if num > 0:
    print("正の数")
elif num < 0:
    print("負の数")
else:
    print("ゼロ")


# ───────── ② 入力文字が "yes" なら承認 ─────────
# text == "yes" ?
#   ├─ Yes → 「承認」
#   └─ No  → 「拒否」
text = input("文字を入力: ")
if text == "yes":
    print("承認")
else:
    print("拒否")


# ───────── ③ 偶数か奇数か ─────────
# num % 2 == 0 ?
#   ├─ Yes → 「偶数」
#   └─ No  → 「奇数」
num = int(input("数を入力: "))
if num % 2 == 0:
    print("偶数")
else:
    print("奇数")


# ───────── ④ "admin" なら管理者 ─────────
# user == "admin" ?
#   ├─ Yes → 「管理者」
#   └─ No  → 「一般」
user = input("ユーザー名: ")
if user == "admin":
    print("管理者")
else:
    print("一般")


# ───────── ⑤ 年齢で成人判定 ─────────
# age >= 20 ?
#   ├─ Yes → 「成人」
#   └─ No  → 「未成年」
age = int(input("年齢: "))
if age >= 20:
    print("成人")
else:
    print("未成年")


# ───────── ⑥ 点数で合格判定 ─────────
# score >= 60 ?
#   ├─ Yes → 「合格」
#   └─ No  → 「不合格」
score = int(input("点数: "))
if score >= 60:
    print("合格")
else:
    print("不合格")


# ───────── ⑦ 文字列長さ判定 ─────────
# len(text) >= 10 ?
#   ├─ Yes → 「長い文字列」
#   └─ No  → 何も表示しない
text = input("文字列を入力: ")
if len(text) >= 10:
    print("長い文字列")


# ───────── ⑧ 入力が空文字か ─────────
# text == "" ?
#   ├─ Yes → 「入力なし」
#   └─ No  → 入力内容をそのまま表示
text = input("入力してください: ")
if text == "":
    print("入力なし")
else:
    print("入力あり:", text)


# ───────── ⑨ 3の倍数ならFizz ─────────
# num % 3 == 0 ?
#   ├─ Yes → 「Fizz」
#   └─ No  → 何も表示しない
num = int(input("数を入力: "))
if num % 3 == 0:
    print("Fizz")

# ───────── ⑩ FizzBuzz ─────────
# スタート
# 1. ユーザーに数値を入力させる
num = int(input("数を入力: "))

# 2. 数値が 3 の倍数かつ 5 の倍数か？
if num % 3 == 0 and num % 5 == 0:
    # Yes → "FizzBuzz" を出力
    print("FizzBuzz")
# 3. 数値が 3 の倍数か？
elif num % 3 == 0:
    # Yes → "Fizz" を出力
    print("Fizz")
# 4. 数値が 5 の倍数か？
elif num % 5 == 0:
    # Yes → "Buzz" を出力
    print("Buzz")
# 5. 上記条件に当てはまらない場合
else:
    # そのまま数値を出力
    print(num)

# 終了

# ───────── ⑪ 果物判定 ─────────
# text in ["apple","banana","orange"] ?
#   ├─ Yes → 「果物」
#   └─ No  → 「その他」
text = input("文字を入力: ")
if text in ["apple", "banana", "orange"]:
    print("果物")
else:
    print("その他")


# ───────── ⑫ 数値の大きさ分類 ─────────
# num >= 100 → 「大きい」
# num >= 50  → 「中くらい」
# それ以外  → 「小さい」
num = int(input("数を入力: "))
if num >= 100:
    print("大きい")
elif num >= 50:
    print("中くらい")
else:
    print("小さい")


# ───────── ⑬ リストに "Python" 含まれるか ─────────
# "Python" in items ?
#   ├─ Yes → 「含まれている」
#   └─ No  → 「含まれていない」
items = ["Java", "Python", "C++"]
if "Python" in items:
    print("含まれている")
else:
    print("含まれていない")


# ───────── ⑭ y/Y で Yes ─────────
# text in ["y","Y"] ?
#   ├─ Yes → 「Yes」
#   └─ No  → 「No」
text = input("入力(y/n): ")
if text in ["y", "Y"]:
    print("Yes")
else:
    print("No")


# ───────── ⑮ 負・ゼロ・正の判定 ─────────
# num < 0 → 「負」
# num == 0 → 「ゼロ」
# num > 0 → 「正」
num = int(input("数を入力: "))
if num < 0:
    print("負")
elif num == 0:
    print("ゼロ")
else:
    print("正")


# ───────── ⑯ 母音かどうか ─────────
# text in ["a","e","i","o","u"] ?
#   ├─ Yes → 「母音」
#   └─ No  → 「子音」
text = input("文字を入力: ")
if text.lower() in ["a","e","i","o","u"]:
    print("母音")
else:
    print("子音")


# ───────── ⑰ ユーザー名とパスワード一致 ─────────
# user=="admin" and pw=="1234" ?
#   ├─ Yes → 「ログイン成功」
#   └─ No  → 「ログイン失敗」
user = input("ユーザー名: ")
pw = input("パスワード: ")
if user == "admin" and pw == "1234":
    print("ログイン成功")
else:
    print("ログイン失敗")


# ───────── ⑱ うるう年判定 ─────────
# (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 ?
#   ├─ Yes → 「うるう年」
#   └─ No  → 「平年」
year = int(input("西暦: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("うるう年")
else:
    print("平年")


# ───────── ⑲ リストが空か ─────────
# len(items) == 0 ?
#   ├─ Yes → 「要素なし」
#   └─ No  → 「n個の要素」
items = [1, 2, 3]
if len(items) == 0:
    print("要素なし")
else:
    print(len(items), "個の要素")


# ───────── ⑳ 文字列が数値か ─────────
# text.isdigit() ?
#   ├─ Yes → 「数値文字列」
#   └─ No  → 「非数値」
text = input("文字を入力: ")
if text.isdigit():
    print("数値文字列")
else:
    print("非数値")

# ───────── ㉑ 英字のみか ─────────
# text.isalpha() ?
#   ├─ Yes → 「アルファベット」
#   └─ No  → 「その他」
text = input("文字列: ")
if text.isalpha():
    print("アルファベット")
else:
    print("その他")


# ───────── ㉒ 3つの数の最大値 ─────────
# if 文で最大を探す
a = int(input("数a: "))
b = int(input("数b: "))
c = int(input("数c: "))
max_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c
print("最大:", max_val)


# ───────── ㉓ リスト全要素が正か ─────────
# all(x > 0 for x in items) ?
#   ├─ Yes → 「OK」
#   └─ No  → 「NG」
items = [1, 2, -3, 4]
if all(x > 0 for x in items):
    print("OK")
else:
    print("NG")


# ───────── ㉔ 回文判定 ─────────
# text == text[::-1] ?
#   ├─ Yes → 「回文」
#   └─ No  → 「回文でない」
text = input("文字列: ")
if text == text[::-1]:
    print("回文")
else:
    print("回文でない")


# ───────── ㉕ 素数判定 ─────────
num = int(input("数を入力: "))
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print("素数")
else:
    print("素数ではない")


# ───────── ㉖ パスワード強度 ─────────
pw = input("パスワード: ")
if len(pw) >= 8 and any(c.isdigit() for c in pw):
    print("強いパスワード")
else:
    print("弱いパスワード")


# ───────── ㉗ 成績評価 ─────────
score = int(input("点数: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")


# ───────── ㉘ 大文字小文字両方含むか ─────────
text = input("文字列: ")
if any(c.islower() for c in text) and any(c.isupper() for c in text):
    print("両方含む")
else:
    print("含まれていない")


# ───────── ㉙ 辞書にキー "id" ─────────
data = {"id": 101, "name": "Taro"}
if "id" in data:
    print("OK")
else:
    print("NG")


# ───────── ㉚ 現在の時間で挨拶 ─────────
import datetime
now = datetime.datetime.now()
if now.hour < 12:
    print("Good morning")
else:
    print("Good afternoon")
