import jwt
import datetime

SECRET = "secret_key"

payload = {
    "user":"admin",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
}

token = jwt.encode(payload, SECRET, algorithm="HS256")

decoded = jwt.decode(token, SECRET, algorithms=["HS256"])
print(decoded)