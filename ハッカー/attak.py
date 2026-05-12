import subprocess
import time
import random

PORT = 1054

i = 0
while True:
    domain = f"test{random.randint(1,99999999)}.local"
    print("[SEND]", domain)

    subprocess.run(
        ["dig", "@127.0.0.1", "-p", str(PORT), domain],
        stdout=subprocess.DEVNULL
    )
    time.sleep(0.01)
