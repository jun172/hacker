import http.client
import json
# 接続先
conn = http.client.HTTPConnection("jsonplaceholder.typicode.com")
#GETリクエスト
conn.request("GET","/posts/1")
responce = conn.getresponse()

print("ステータス:",responce.status)
data = responce.read()
print("レスポンス:",data.decode())

conn.close()