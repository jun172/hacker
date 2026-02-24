import requests
def send_siem(event):
    requests.post(
        "http://siem:9200/soc-events/_doc",
        json=event
    )