import socket

def tcp_connect(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    sock.connect((host, port))
    return sock


def fetch_http_raw(sock, host):
    req = (
        f"GET / HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"User-Agent: ReconFramework\r\n"
        f"Connection: close\r\n\r\n"
    )
    sock.send(req.encode())

    data = b""
    while True:
        chunk = sock.recv(4096)
        if not chunk:
            break
        data += chunk

    return data.decode(errors="ignore")


def parse_headers(raw):
    header_block = raw.split("\r\n\r\n")[0]
    headers = {}

    for line in header_block.split("\r\n")[1:]:
        if ":" in line:
            k, v = line.split(":", 1)
            headers[k.strip().lower()] = v.strip()

    return headers


LIBRARY_SIGS = {
    "apache": ["apache"],
    "nginx": ["nginx"],
    "iis": ["microsoft-iis"],
    "php": ["php"],
    "express": ["express"],
    "node": ["node"],
    "cloudflare": ["cloudflare"],
    "openresty": ["openresty"],
    "wordpress": ["wp-", "wordpress"],
    "laravel": ["laravel"]
}


def detect_libraries(headers):
    found = []
    banner = headers.get("server", "") + " " + headers.get("x-powered-by", "")

    for lib, sigs in LIBRARY_SIGS.items():
        for s in sigs:
            if s.lower() in banner.lower():
                found.append(lib)

    return found


def get_banner_url(headers):
    return headers.get("location", "none")


def web_fingerprint(host, port):
    try:
        sock = tcp_connect(host, port)
        raw = fetch_http_raw(sock, host)
        headers = parse_headers(raw)

        print("\n--- HTTP Banner ---")
        print("Server:", headers.get("server", "unknown"))
        print("X-Powered-By:", headers.get("x-powered-by", "unknown"))

        libs = detect_libraries(headers)
        print("Detected Libraries:", ", ".join(libs) if libs else "none")

        print("Redirect URL:", get_banner_url(headers))

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python HTTP.py <host> <port>")
        print("Example: python HTTP.py example.com 80")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])

    web_fingerprint(host, port)
