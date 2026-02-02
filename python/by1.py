import hashlib

password = "mypassword"
hashd = hashlib.sha256(password.encode()).hexdigest()

input_pw = "mypassword"
if hashlib.sha256(input_pw.encode()).hexdigest() == hashd:
    print("認証成功")