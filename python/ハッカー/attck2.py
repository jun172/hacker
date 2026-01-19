import subprocess
import random 
import time 

PORT = 1054

while True:
    domain = f"rand{random.randint(1,10000000)}.local"
    subprocess.run(
        ["dig","@127.0.0.1","-p",str(PORT),domain],
        stdout=subprocess.DEVNULL
    )
    time.sleep(0.05)