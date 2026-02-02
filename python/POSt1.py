import requests
url="https://httpbin.org/post"

data = {
    "userneme":"testuser",
    "password":"1234"
}
respose = requests.post(url,data=data)
print(respose.json())
