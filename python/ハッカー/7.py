import subprocess
import re 

def get_local_ip():
    result = subprocess.check_output(["ifconfig","en0"]).decode()
    
    match = re.search(r"inet (\d+\.\d+\.\d+\.\d+)", result)
    if match:
        return match.group(1)
    
    else:
        return None
    
ip = get_local_ip()
print("Your lacal IP:",ip)