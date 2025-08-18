# -----------------------------
# 基礎問題（ウォーミングアップ）
# -----------------------------

# 1. 変数の計算
x = 7
c = x * 2
print(c)   # → 14

# 2. リストの合計
mylist = [3, 6, 9]
print(sum(mylist))   # → 18

# 3. 偶数判定（0〜9）
for i in range(0, 10):
    if i % 2 == 0:
        print(i, 'は偶数')

# 4. 文字列を大文字に変換
sont = 'heijffbsjc'
print(sont.upper())  # → HEIJFFBSJC

# 5. 二乗関数
def square(n):
    return n ** 2

print(square(2))   # → 4
