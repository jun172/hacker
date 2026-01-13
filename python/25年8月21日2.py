# =======================================
# 1. リスト処理 -> 平均値の計算
# =======================================
mylist = [1, 2, 3, 4, 5]
ave = sum(mylist) / len(mylist)
print("平均値:", ave)


# =======================================
# 2. 標準化 (scikit-learn)
# =======================================
import numpy as np
from sklearn.preprocessing import StandardScaler

mylist = np.array([[1], [2], [3], [4], [5]])  # fit_transformは2次元配列が必要
scaler = StandardScaler()
scaled_data = scaler.fit_transform(mylist)
print("標準化されたデータ:", scaled_data)


# =======================================
# 3. データフレーム処理 (pandas)
# =======================================
import pandas as pd

mylist = [5, 4, 3, 2, 1]
df = pd.DataFrame(mylist, columns=["numbers"])
print("データフレーム:\n", df)


# =======================================
# 4. 散布図の表示 (ランダムデータ)
# =======================================
import matplotlib.pyplot as plt

x = np.random.rand(10)
y = np.random.rand(10)

plt.scatter(x, y)
plt.title("散布図")
plt.xlabel("x軸")
plt.ylabel("y軸")
plt.show()


# =======================================
# 5. 身長と体重の散布図
# =======================================
X = np.array([131, 132, 132, 133.5, 135, 142, 143.8, 144, 148, 149, 
              150, 152, 153, 157, 158, 158, 162, 164, 166, 169, 
              169.5, 170, 172, 173, 173, 176, 180, 184, 186, 190])
Y = np.array([31, 28, 35, 40, 31, 40, 42, 45, 50, 48, 
              56, 50, 51, 56, 65, 61, 66, 61.5, 69, 71, 
              63, 68, 80, 74, 76.5, 82, 68, 75, 92, 90])

plt.scatter(X, Y)
plt.xlabel("身長 [cm]")
plt.ylabel("体重 [kg]")
plt.title("身長と体重の散布図")
plt.show()


# =======================================
# 6. 線形回帰モデルで予測
# =======================================
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Xは2次元配列に reshape
X = X.reshape(-1, 1)
Y = Y

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

model = LinearRegression()
model.fit(x_train, y_train)

# 新しい入力値で予測
new_height = np.array([[175]])  # 175cmの人を予測
predicted_weight = model.predict(new_height)
print("175cmの予測体重:", predicted_weight[0])


# =======================================
# 7. モジュール -> 交差検証 (Irisデータ)
# =======================================
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

iris = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)

logreg = LogisticRegression(max_iter=200).fit(x_train, y_train)
score = logreg.score(x_test, y_test)
print("テストスコア:", score)


# =======================================
# 8. データ読み込み & 欠損値処理
# =======================================
df = pd.DataFrame({
    "A": [1, 2, None],
    "B": [4, None, 6],
    "C": [None, None, None]
})
print("欠損値を含むデータ:\n", df)
print("全てNaNの行を削除:\n", df.dropna(how="all"))


# =======================================
# 9. ランダムに並び替え
# =======================================
import random
x = [0, 1, 2, 3, 4]
x_shuffled = random.sample(x, len(x))
print("シャッフル:", x_shuffled)
print("元のリスト:", x)


#学習済みモデルを使って未知のデータを入力したときに、予測結果を出す処理
# 線形回帰で「身長から体重を予測する」例
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 学習データ（身長と体重）
X = np.array([150, 155, 160, 165, 170, 175, 180]).reshape(-1, 1)  # 特徴量（身長）
Y = np.array([50, 55, 60, 65, 70, 75, 80])  # 目的変数（体重）

# モデルを作成・学習
model = LinearRegression()
model.fit(X, Y)

# ===== ここがポイント =====
# 新しい入力値で予測
new_height = np.array([[172]])   # 172cmの人
predicted_weight = model.predict(new_height)

print("新しい入力値:", new_height[0][0], "cm")
print("予測された体重:", predicted_weight[0], "kg")

# グラフ表示
plt.scatter(X, Y, color="blue", label="学習データ")
plt.plot(X, model.predict(X), color="red", label="回帰直線")
plt.scatter(new_height, predicted_weight, color="green", label="予測点", s=100)
plt.xlabel("身長 [cm]")
plt.ylabel("体重 [kg]")
plt.legend()
plt.show()


# 開始
#   │
#   ▼
# リスト [1,2,3,4,5] の平均を計算
#   │
#   ▼
# リスト [1,2,3,4,5] を標準化（平均0, 分散1）
#   │
#   ▼
# リスト [1,2,3,4,5] と [5,4,3,2,1] の相関係数を計算
#   │
#   ▼
# CSV ファイル data.csv の列 X と Y の散布図を描く
#   │
#   ▼
# 線形回帰の単純モデルを作り、予測値を計算
#   │
#   ▼
# sklearn を使い、リスト [0,1,0,1] をラベル分類
#   │
#   ▼
# 交差検証でモデルの精度を計算
#   │
#   ▼
# pandas データフレームで NaN を含む行を削除
#   │
#   ▼
# データをランダムにシャッフルして分割（訓練・テスト）
#   │
#   ▼
# 新しい入力値で予測を行い、結果を出力
#   │
#   ▼
# 終了
