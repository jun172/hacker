# --- 1. 正負ゼロ判定 ---
# フローチャート:
# [開始] → [数字入力] → [num > 0 ?]
#   ├→ YES → [正の数と表示] → [終了]
#   ├→ NO → [num < 0 ?]
#         ├→ YES → [負の数と表示] → [終了]
#         └→ NO → [ゼロと表示] → [終了]

use = int(input('数字を入力してください: '))  
if use > 0:
    print('正の数')
elif use < 0:
    print('負の数')
else:
    print('ゼロ')


# --- 2. FizzBuzz ---
# フローチャート:
# [開始] → [1〜100をループ]
#   → [iが3と5の両方で割れるか?]
#        ├→ YES → [Fizz Buzz]
#        └→ NO → [iが3で割れるか?]
#                ├→ YES → [Fizz]
#                └→ NO → [iが5で割れるか?]
#                        ├→ YES → [Buzz]
#                        └→ NO → [iをそのまま表示]
#   → [次のiへ] → [終了]

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('Fizz Buzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)


# --- 3. 母音カウント ---
# フローチャート:
# [開始] → [文字列入力] → [母音リスト(aeiou)]
#   → [各母音vについて繰り返し]
#       → [文字列.count(v)で数える]
#       → [結果を出力]
#   → [終了]

sur = input('文字列を入力してください: ')
vowels = "aeiou"
for v in vowels:
    print(f"{v}: {sur.count(v)}")


# --- 4. 偶数リストと合計 ---
# フローチャート:
# [開始] → [1〜50の数列を作る]
#   → [偶数だけ抽出]
#   → [偶数リストを表示]
#   → [合計を計算して表示]
#   → [終了]

nums = [i for i in range(1, 51) if i % 2 == 0]
print("偶数リスト:", nums)
print("合計:", sum(nums))


# --- 5. 九九表 ---
# フローチャート:
# [開始] → [a=1〜9ループ]
#   → [b=1〜9ループ]
#       → [a×bを計算]
#       → [結果を出力]
#   → [bループ終了 → 改行]
# → [aループ終了 → 終了]

print("九九表")
print("-----")
for a in range(1, 10):
    for b in range(1, 10):
        ans = a * b
        print(f"{a}+{b}={ans}", end="\t")
    print("")
