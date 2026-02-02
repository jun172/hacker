import requests

url="https://jsonplaceholder.typicode.com/comments"
parms = {"postId":1}

response = requests.get(url, params=parms)
print(response.json())