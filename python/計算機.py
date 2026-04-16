import tkinter as tk
import math

# 計算ロジック
def click_button(value):
    entry_var.set(entry_var.get() + str(value))

def clear_entry():
    entry_var.set("")

def calculate():
    try:
        # 安全のため math 関数を eval の環境に追加
        expr = entry_var.get()
        result = eval(expr, {"__builtins__":None}, math.__dict__)
        entry_var.set(str(result))
    except Exception:
        entry_var.set("エラー")

# Tkinterウィンドウ
root = tk.Tk()
root.title("科学計算機")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=5, pady=10)

# ボタン一覧
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3), ('sqrt(',1,4),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3), ('**',2,4),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3), ('log(',3,4),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3), ('C',4,4),
    ('sin(',5,0), ('cos(',5,1), ('tan(',5,2), ('pi',5,3), ('e',5,4)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 12), command=calculate)
    elif text == 'C':
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 12), command=clear_entry)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 12), command=lambda t=text: click_button(t))
    btn.grid(row=row, column=col, padx=3, pady=3)

root.mainloop()