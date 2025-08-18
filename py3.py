# 0〜10まで出力
for i in range(11):
    print(i)

# 1〜100までの合計を求める
total = 0
for i in range(101):
    total += i
print("合計:", total)

# 入力が偶数か奇数か判定
c = int(input('入力してください: '))
if c % 2 == 0:
    print('偶数')
else:
    print('奇数')

# ユーザー入力で range を使う
sore = int(input('数字を入力してください: '))
for i in range(sore):
    print(i)

# リストの合計
car = [1,2,3,4,5]
print(sum(car))

# 平均値
kai = [10,20,30,40,50]
avg = sum(kai)/len(kai)
print("The average is", round(avg, 2))

# 文字列メソッド
py = "python"
print(py.isupper())  # () をつける必要あり

# 部分文字列のカウント
l = "hello world"
print(l.count('o'))

# 関数: 2乗を返す
def square(n):
    return n**2
print(square(5))

# 素数判定（2だけでなく一般化する）
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(7))

# タプル
tapule_ka = (5, 10, 15)
print(tapule_ka)

# 1〜20の中で3の倍数を出力
for i in range(1, 20):
    if i % 3 == 0:   # ←修正
        print(i)

# 辞書アクセス
zisi = { "apple":100, "banana":200 }
print(zisi["apple"])  # インデックスではなくキーでアクセス

# 入力終了
use_input = input('入力してください: ')
if use_input == "exit":
    print("終了しました")
    exit()

# クラス
class Car:
    def __init__(self, name):
        self.name = name

my_car = Car("Toyota")
print(my_car.name)

class Person:
    def greet(self, name):
        print(name + "です")

p = Person()
p.greet("田中")

# ランダム値
import random
for i in range(7):
    print(random.randint(1,100))

# リスト操作
ri = [1,2,3,4,5]
new = [x*2 for x in ri]
print(new)

# 回文判定
string = input("文字列を入力してください: ")
if string == string[::-1]:
    print("この文字列は回文です")
else:
    print("この文字列は回文ではありません")

# ソート
fige = [3,1,4,1,5,9]
fige.sort()
print(fige)


