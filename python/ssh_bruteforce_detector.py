import time
import re
from collections import defaultdict
from datetime import datetime, timedelta

LOG_FILE = "/var/log/auth.log"
THRESHOLD = 5 # 失敗回数
WINDOW_SECONDS = 60  #監視時間（秒）

failed_pattern = re.compile(
    r"Failed password.*from (?P<ip>\d+\.\d+\.\d+)"
)

attempts = defaultdict(list)

def alert(ip, count):
    print(f"[ALERT] SSH Bruteforece detected | IP={ip} | attempts={count}")

def follow(file):
    file.seek(0,2)
    while True:
        line =  file.readline()
        if not line:
            time.sleep(0.2)
            continue
        yield line
        
def main():
    print("[SOC] SSH Bruteforce Detector started")
    
    with open(LOG_FILE, "r") as f:
        loglines = follow(f)
        
        for line in loglines:
            match = failed_pattern.search(line)
            if not match:
                continue
            
            ip = match.group("ip")
            now = datetime.now()
            
            attempts[ip] = [
                t for t in attempts[ip]
                if now - t < timedelta(seconds=WINDOW_SECONDS)
            ]
            
            attempts[ip].append(now)
            
            if len(attempts[ip]) >= THRESHOLD:
                alert(ip, len(attempts[ip]))
                attempts[ip].clear() #二重アラート防止

if __name__ == "__main__":
    main()