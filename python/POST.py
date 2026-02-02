import requests
url = "https://jsonplaceholder.typicode.com/posts"
# 送信データ
payload = {
    "title": "Python",
    "body": "HTTPリクエスト送信テスト",
    "userId": 1
}
response = requests.post(url, json=payload)
print("ステータスコード:", response.status_code)
print("レスポンス:", response.json())