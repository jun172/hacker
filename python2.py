# ==========================================
# ハッキング基礎 Python 10問練習
# ==========================================

# 1. 変数代入
# 変数 port に 80 を代入し、その値を表示
port = 80
print(port)

# 2. 文字列操作
# 変数 ip に IPアドレスを代入し、表示
ip = "192.168.1.1"
print(ip)

# 3. 四則演算（割り算と余り）
# 変数 a=15, b=4 の割り算結果と余りを表示
a = 15
b = 4
print("割り算:", a / b)
print("余り:", a % b)

# 4. リスト操作
# targets の要素数を len() で取得して表示
targets = ["host1", "host2", "host3"]
print("要素数:", len(targets))

# 5. タプル操作
# ports の最後の要素を表示
ports = (22, 80, 443)
print("最後の要素:", ports[-1])

# 6. 辞書操作
# scanner 辞書から "tool" を取得して表示
scanner = {"tool": "nmap", "version": 7}
print("ツール名:", scanner["tool"])

# 7. 条件分岐
# status_code が 200 なら成功、それ以外は失敗を表示
status_code = 200
if status_code == 200:
    print("成功")
else:
    print("失敗")

# 8. forループ
# ports の要素を順番に表示
ports = [21, 22, 23, 25]
for p in ports:
    print(p)

# 9. whileループ
# count が 5 未満の間、count を表示して1ずつ増やす
count = 0
while count < 5:
    print(count)
    count += 1

# 10. 偶数判定
# packet_size が偶数か奇数か判定して表示
packet_size = 128
if packet_size % 2 == 0:
    print("偶数")
else:
    print("奇数")
