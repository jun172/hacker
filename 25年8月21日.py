#1. サイバー攻撃系・解析系（ログ解析、安全演習）

#入力->条件分離->出力
use_name=int(input('数値を入力'))
if use_name >0:
    print('正の数')
elif use_name <0:
    print('負の数')
else:
    print('ゼロ')
    
#入力->ファイル処理->出力
with open ("access.log","r",encoding="utf-8") as f:
    file=f.read("error")
    print("access.log")
    print(file)
    
#入力->モジュール->ファイル処理->for文回転->出力
import re

ip_adress=["192.168.0.1"]
with open ("access.log","r",encoding="utf-8") as f:
    for line in f:
        ips=re.findall("192.168.0.1",line)
        ip_adress.extend(ips)

#入力->def関数条件分離->出力
tyoe=input("入力")

def  get_mozi (DROPTABLE):
    if DROPTABLE ==DROPTABLE:
        print("含まれている")
    else:
        print("含まれていない")
get_mozi("DROP TABLE")

#入力->条件分離->終了
with open ("users.txt","r",encoding="utf-8") as f:
    for pasword in f:
        if pasword <8:
            print("弱い")
            
#モジュール->ファイル処理->ハッシュ化処理->出力
import hashlib

listk=[]
if not all(ch in "0127druHSWKD" for ch in listk) or len(listk) !=64:
    hashrd=hashlib.sha512(listk.encode()).hexdigest()
    with open ("config.txt","w",encoding="utf-8") as f:
        f.write(hashrd)
        print("config.txt をハッシュ化して保存んしました")
else:
    print("すでにハッシュ済み")

#入力->URL取得->条件分離->はい-->出力
                #|          |
                #->いいえ ---^
import re
URL= input("URLを入力してください:")

if re.match("http://",URL):
    print("安全ではない通信")
elif re.match("https://",URL):
    print("暗号化通信",URL)
else:
    print("不明なURL形式です")

#def関数->条件分離->出力
import os 
import random
import string
import hashlib
def password (size=3):
    ched =string.ascii_letters+ string.digits+ string.ascii_uppercase
    return ''.join(random.choice(ched) for _ in range(size))

print("自動生成パスワード:", password(3))
print("\n")

#モジュール->リスト処理->ファイル処理->for文回転->変数ip->出力
import re
ip_list=[]
with open("access.log","r", encoding="utf-8") as f:
    for line in f:
        ips = re.findall(r"\b(?:[-9]{1,3}\.){3}[0-9]{1,3}\b", line)
        ip_list.extend(ips)
        
#入力->回文判定->出力
strig = input("回文判定する文字列を入力してください:")

if string == string[::-1]:
    print("回文です")
else:
    print("回文ではありません")
    
