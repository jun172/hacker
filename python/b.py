import itertools
import string
import time

# 本来はサーバ側にある情報
REAL_PASSWORD = "aaa"

# 攻撃側の設定
chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
max_len = 100

attempts = 0
start = time.time()

for lenght in range(1,max_len + 1):
    for combo in itertools.product(chars, repeat=lenght):
        guess = "".join(combo)
        attempts += 1
        
        print(f"試行 {attempts}: {guess}")
        
        if guess == REAL_PASSWORD:
            print("✅ パスワード発見！:", guess)
            print("⏱ 所要時間:", round(time.time() - start, 2), "秒")
            exit()

print("❌ 見つかりませんでした")