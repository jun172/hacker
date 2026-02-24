
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from utils import banner

def check_directory(base_url, word):
    url = f"{base_url.rstrip('/')}/{word}"
    try:
        r = requests.get(url, timeout=2)
        if r.status_code != 404:
            return f"{url} -> {r.status_code} ({len(r.text)} bytes)"
    except:
        return None

def dir_enum(base_url):
    banner("DIRECTORY ENUMERATION (THREADED)")

    wordlist = [
        "admin", "login", "dashboard", "test", "backup",
        "uploads", "config", "api", "dev", "old"
    ]

    results = []

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(check_directory, base_url, word) for word in wordlist]

        for future in as_completed(futures):
            result = future.result()
            if result:
                print(result)
