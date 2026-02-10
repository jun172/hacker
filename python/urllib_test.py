from urllib import request, parse
import json

# GETリクエスト
url = "https://jsonplaceholder.typicode.com/posts/1"
with request.urlopen(url) as response:
    data = json.load(response)
    print(data)
#POSTリクエスト
url = "https://jsonplaceholder.typicode.com/posts"
post_data = parse.urlencode({
    "title":"Python",
    "body":"urllib POST",
    "userId":1
}).encode()

req = request.Request(url, data=post_data)
with request.urlopen(req) as responce:
    result = json.load(responce)
    print(result)
    
