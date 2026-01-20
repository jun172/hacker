import subprocess
import random
import time 

DNS_SERVER = "127.0.0.1"
PORT = "1054"

print("[*] DNS brute-force simulator started (LOCAL ONLY)")

while True:
    name= f"rand{random.randint(1000000,9999999)}{random.randint(1000000,99999999)}"
    subprocess.run(
        ["dig",f"@{DNS_SERVER}","-p",PORT, name],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    time.sleep(0.05)