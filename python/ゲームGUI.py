import tkinter as tk
import random

answer = random.randint(1, 10)

#判定関数
def check_bumber():
    guess = int(entry.get())
    
    if guess == answer:
        result_label.config(text="正解")
    elif guess < answer:
        result_label.config(text="最も大きい数字です")
    else:
        result_label.config(text="最も小さい数字です")
        
#メイン画面
root = tk.Tk()
root.title("数当てゲーム")
root.geometry("300x200")

#説明文
label = tk.Label(root, text="1~10の数字を当ててください")
label.pack(pady=10)

#入力ボックス
entry = tk.Entry(root)
entry.pack(pady=10)

#判定ボタン
button = tk.Button(root, text="判定", command=check_bumber)
button.pack(pady=10)

#結果表示
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

#画面表示
root.mainloop()