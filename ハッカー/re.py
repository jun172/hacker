import requests
URL="http://127.0.0.1:5000/"
while True:
    r = requests.get(URL)
    print(r.status_code)