import random

answer = random.randint(1,10)

while True:
    guess = int(input("1~10の数字入力してください"))
    
    if guess == answer:
        print("正解!")
        break
    elif guess < answer:
        print("最も大きい数字です")
    else:
        print("最も小さい数字です")