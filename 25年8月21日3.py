# =====================================
# 演習問題セット
# =====================================

# 問題6: NumPy・配列操作
# 1～100 の整数配列を作成し、偶数だけ抽出して平均値を計算せよ。
import numpy as np
arr = np.arange(1, 101)
even = arr[arr % 2 == 0]
print("偶数の平均:", even.mean())


# 問題7: Pandas・データ分析
# CSV ファイル data.csv を読み込み、欠損値を削除した後、特定の列 X と Y の散布図を描画せよ。
import pandas as pd
import matplotlib.pyplot as plt
# df = pd.read_csv("data.csv")
# df = df.dropna()
# plt.scatter(df["X"], df["Y"])
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.show()


# 問題8: オブジェクト指向
# BankAccount クラスを作成し、deposit, withdraw, balance を実装せよ。
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("残高不足です")
        self._balance -= amount

    def balance(self):
        return self._balance


# 問題9: scikit-learn・機械学習
# X=[[1],[2],[3],[4]], y=[2,4,6,8] の線形回帰モデルを作成し、新しい入力 [[5]] の予測値を出力。
from sklearn.linear_model import LinearRegression
X = [[1],[2],[3],[4]]
y = [2,4,6,8]
model = LinearRegression().fit(X, y)
print("予測:", model.predict([[5]])[0])


# 問題10: 乱数・アルゴリズム
# 0～9 の数字をランダムに 6 桁生成し、重複なしのリストを作成。
import random
digits = random.sample(range(10), 6)
print("ランダム6桁:", digits)


# =====================================
# 補足サンプルコード
# =====================================

# 1. 回文チェック
message = input("Enter a message: ")
if message == message[::-1]:
    print(message.upper(), "→ 回文です")
else:
    print("回文ではありません")

# 2. 辞書データ処理
data = {"a": 10, "b": 55, "c": 40, "d": 75}
for key, value in data.items():
    if value > 50:
        print(f"{key}の値は{value}で50より大きいです")
    else:
        d = dict(k1=key, k2=value)
        print(d)

# 3. 例外処理付き入力
try:
    s = int(input("スコアを入力してください: "))
    print("入力スコア:", s)
except ValueError:
    print("無効な入力です。")

# 4. ハッシュ化
import hashlib
usr = input("ユーザー名を入力してください: ")
hs_sha256 = hashlib.sha256(usr.encode()).hexdigest()
hs_sha512 = hashlib.sha512(usr.encode()).hexdigest()
print("SHA-256:", hs_sha256)
print("SHA-512:", hs_sha512)

# 5. NumPy 配列サンプル
li = np.arange(1, 101)
print("最初の10個:", li[:10])

