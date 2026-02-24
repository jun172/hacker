import datetime

def log(msg):
    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def banner(title):
    print("=" * 50)
    print(f" {title}")
    print("=" * 50)
