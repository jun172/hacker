import csv #ファイル操作
import datetime #データモジュール
import itertools #ループ処理の時に便利なジェネレータをたくさん持っている箱

# 1. CSVファイル data.csv を読み込み、1列目の合計値を出力せよ。
with open ("data.csv","r",encoding="utf-8") as f:#ファイル操作
    reader=csv.reader(f)#変数にモジュール
    total=sum(int(row[0])for row in reader if row)#readerから各行を取り出し、空行を除外して1列目を整数化して合計
print("1列目の合計:",total)#表示

# 2. 辞書から値が5以上の果物をリストで出力せよ
fruits= {"りんご":3,"みかん":5,"バナナ":2}#辞書
print([k for k, v in fruits.items() if v >= 5])# fruits の中で値が5以上のキーをリストにする

#3. 偶数だけを抽出
lst=[10,20,30,40,50]
print([x for x in lst if lst % 2==0])# x には lst から1つずつ取り出した値が入る
# 4. CSVにある商品名と数量を辞書に変換せよ。
with open ("","r",encoding="utf-8") as f:
    reader= csv.reader(f)
    product_dict={row[0]:int[row[1]]for row in reader if row}# row[0] をキー (商品名など)、row[1] を整数に変換して値にする
print(product_dict)
#5. ネストした辞書の全商品合計
d={"店A":{"りんご":5,"みかん":2},"店B":{"りんご":3}}
print(sum(sum(v.valuse())for v in d.values()))#   sum(v.values()) : 内側の辞書 v の value を合計
#6. リストを辞書に変換し、値は文字数にせよ。
words=["apple","banana","orenge"]
print({w:len(w) for w in words})# w には words の要素（単語）が1つずつ入る
#7. 辞書のキーをすべて大文字に
d={"apple":1,"banana":2}
print({k.upper(): v for k, v in d.items()})# k には辞書のキーが入る items辞書の中の全ての (キー, 値) の組を返す
# 8. CSVファイルの各行の合計をリストに格納
with open ("data.csv","r",encoding="utf-8") as f:
    reader=csv.reader(f)
    row_swms=[sum(map(int,row))for row in reader if row]#if row 有効な行だけ処理する sum(map(int, row))整数に変換した行の値を合計   CSV reader から読み込んだ各行の合計値を計算してリスト化 
print(row_swms)
# 9. 重複削除
l=[10,20,30,40,50]
print(list(sum(l)))
# 10. 辞書の値の最大値
d={"a":5,"b":12,"c":8}
print(max(d.values()))
#11. CSVにある日付列を datetime 型に変換
with open ("data.txt","r",encoding="utf-8") as f:
    reader= csv.reader(f)
    dates=[datetime.datetime.strptime(row[0],"%Y-%m-%d")for row in reader if row]#日付オブジェクト datetime.datetime.strptime(row[0], "%Y-%m-%d")  
print(dates)
#12. 累積和
lst=[1,2,3,4]
print(list(itertools.accumulate(lst)))#リストやイテラブルの累積計算を行う関数->itertools.accumulate listは出力だけ
## 13. 辞書の値を2倍
d={"a":2,"b":3}
print({k:v * 2 for k, v in d.items()})#d.items()->キーと値のペア を取り出す for文でk,vを入れる  v * 2　２倍
#14. CSVから特定の列だけを抽出
with open ("data.csv","r",encoding="utf-8") as f:
    reader=csv.reader(f)
    coli=[row[0]for row in reader if row]## reader は CSVの各行をリストとして返す if row 空白とばす有効を入れる 
print(coli)
#15. 文字列を長さ順にソート
word=["apple","banana","kiwi","orengi"]
print(sorted(word,key=len))#文字列の長さ (len)　リスト word の要素を 並べ替える（ソート）

#2️⃣ GUI操作（10問 / Tkinter）
import tkinter as tk #GUIpythonでの操作モジュール
from tkinter import messagebox #メッセージボックスを表示するためのモジュール です。
import random
import datetime

# 1. 名前入力 → 「こんにちは〇〇」
def hello_app():
    root = tk.Tk()#メインウィンドウ作成
    root.title("挨拶")#タイトル
    tk.Label(root, text="名前を入力:").pack()#Tkinterで画面に文字
    entry= tk.Entry(root)#一行の入力欄->Entry
    entry.pack()
    def greet():
        messagebox.showinfo("挨拶", f"こんにちは {entry.get()}")#入力欄に入力したテキストを取り出して、メッセージボックスに表示する
    tk.Button(root,text="実行", compound=greet).pack()#
    root.mainloop()## イベントループ開始

# 2. 2つの数字を入力 → 合計表示
def add_app():
    root=tk.Tk()
    root.title("電卓")
    e1 = tk.Entry(root);e2=tk.Entry(root)# 入力欄（テキストボックス）を2つ作成
    e1.pack();e2.pack()# 画面に配置
    def cale():
        total=int(e1.get()) + int(e2.get())#数字をゲットされる
        messagebox.showinfo("結果",f"合計: {total}")
    tk.Button(root, text="計算",command=cale).pack()
    root.mainloop()
    
# 3. 入力が空なら「入力なし」
def empty_check_app():
    root=tk.Tk()
    root.title("入力確認")
    e = tk.Entry(root);e.pack()
    def check():
        text= e.get()
        messagebox.showinfo("結果","入力なし" if not text else text)
    tk.Button(root, text="確認",command=check).pack()
    root.mainloop()

# 4. ボタンでランダム数字
def random_app():
    root=tk.Tk()
    root.title("ランダム数")
    def show_rand():
        messagebox.showinfo("数字",str(random.randint(1,100)))
    tk.Button(root,text="数字生成",command=show_rand).pack()
    root.mainloop()
    
# 5. ドロップダウン
def dropdowm_app():
    root=tk.Tk()
    var= tk.StringVar(value="apple")
    menu=tk.OptionMenu(root,var, "apple","banana","orange")
    menu.pack()
    def show():
        messagebox.showinfo("選択",var.get())
    tk.Button(root, text="確認", command=show).pack()
    root.mainloop()

# 6. 入力文字列の長さ
def strlen_app():
    root=tk.Tk()
    e=tk.Entry(root);e.pack()
    def cale():
        messagebox.showinfo("長さ",str(len(e.get())))
    tk.Button(root,text="計算",command=cale).pack()
    root.mainloop()
    
# 7. チェックボックス
def cheakbox_app():
    root=tk.Tk()
    var1, var2=tk.BooleanVar(),tk.BooleanVar()
    tk.Checkbutton(root,text="A",variable=var1).pack()
    tk.Checkbutton(root,text="B",variable=var2).pack()
    def show():
        selected=[]
        if var1.get(): selected.append("A")
        if var2.get(): selected.append("B")
        messagebox.showinfo("選択",str(selected))
    tk.Button(root, text="確認",command=show).pack()
    root.mainloop()
# 8. 偶数奇数判定
def evenodd_app():
    root=tk.Tk()
    e=tk.Entry(root); e.pack()
    def cheak():
        n =int(e.get())
        messagebox.showinfo("判定","偶数" if n % 2 == 0 else "奇数")
    tk.Button(root,text="判定",command=cheak).pack()
    root.mainloop
# 9. スライダー値表示
def slider():
    root=tk.Tk()
    var=tk.IntVar()
    scale=tk.Scale(root,from_=0,to=100,orient="horizontal",variable=var)
    scale.pack()
    def show():
        messagebox.showinfo("値",str(var.get()))
    tk.Button(root, text="確認",command=show).pack()
    root.mainloop
#10. 現在日時を表示
def datetime_app():
    root=tk.Tk()
    def show():
        messagebox.showinfo("日時",str(datetime.datetime.now()))
    tk.Button(root, tezt="現在日時",command=show).pack()
    root.mainloop()
    
#3️⃣ 日付計算（5問）
import datetime
import calendar

# 1. 今日の日付を取得して7日後の日付
today=datetime.data.today()
print("今日は:",today,"7日後:",today+datetime.timedelta(daya=7))
# 2. うるう年判定
year=int(input("西暦を入力:"))
is_leap=(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print("閏年" if is_leap else "平年")
#3. 2つの日付の差
d1 = datetime.date(2025,8,26)
d2 = datetime.date(2025,9,26)
print("差:",(d2-d1).days,"日")
#4. 今日の曜日
week = ["月", "火", "水", "木", "金", "土", "日"]
print("曜日:",week[today.weekday()])
# 5. 入力年月の月末日
y,m=2025,8
last_day=calendar.monthrange(y,m)[1]
print(f"{y}年{m}月の月末日:",last_day)
