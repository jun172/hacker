from cryptography.fernet import Fernet
import os

KEY = open("key.key","rb").read()
cipher = Fernet(KEY)

for file in os.listdir("files"):
    path = f"files/{file}"
    with open(path, "rb") as f:
        data = f.read()
        
    decrypted = cipher.decrypt(data)
    
    with open(path, "wb") as f:
        f.write(decrypted)
        
print("✅ 復号完了")