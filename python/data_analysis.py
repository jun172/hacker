import pandas as pd
import matplotlib.pyplot as plt

#csv読み込み
df = pd.read_csv("sales.csv")

#データ確認
print("一覧")
print(df)

#売上合計
total_sales = df["sales"].sum()
print("総売上:",total_sales)

#部署ごとの売り上げ
departemet_sales = df.groupby("department")["sales"].sum()
print("部署売り上げ")
print(departemet_sales)

#平均売上
avg_sales = df["sales"].mean()
print("平均売上:", avg_sales)

#最大売上
max_sales = df["sales"].max()
print("最大売上:", max_sales)

#グラフ作成
departemet_sales.plot(kind="bar")

plt.title("Department Sales")
plt.xlabel("Department")
plt.ylabel("Sales")

plt.show()