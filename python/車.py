import can 
import time
from collections import defaultdict

#メッセージカウント
packet_count = defaultdict(int)

#最初に観測した時間
start_time = defaultdict(lambda: time.time())

#閾値（ここは調整）
TIME_WINDOW = 5
THRESHOLD = 20

with can.Bus(interface='socketcan',channel='vcan0') as bus:
    for msg in bus:
        msg_id = msg.arbitration_id
        current_time = time.time()
        
        #カウント
        packet_count[msg_id] += 1
        
        #経過時間
        elapsed = current_time - start_time[msg_id]
        
        #一定時間経過したら判定
        if elapsed > TIME_WINDOW:
            if packet_count[msg_id] > THRESHOLD:
                print(f"⚠️ Suspicious ID {msg_id}: {packet_count[msg_id]} msgs in {TIME_WINDOW}s")
                
                #リセット
                packet_count[msg_id] = 0
                start_time[msg_id] = current_time