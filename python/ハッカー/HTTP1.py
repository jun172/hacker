import socket
import dns.resolver

def tep_connect(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    sock.connect((host,port))
    return sock

def fetch_http_raw(sock,host):
    reg=(
        f"GET / HTTP/1.1\r\n"
        f"Host:{host}\r\n"
        f"User-Agent: ReconFramework\r\n"
        f"Connection: closer\r\n\r\n"
        )
    sock.send(reg.endcode())
    
    data =b""
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
            k,v =line.split(":",1)
            headers[k.strip().lower()] = v.strip()
            
    return headers

def is_cloudflare_ip (host):
    try:
        sock = tep_connect(host, 80)
        raw = fetch_http_raw(sock, host)
        headers = parse_headers(raw)
    except:
        return False
    
COMMON_SUBS = {
    "www","mail","ftp","dev","api","old","test",
    "string","direct","admin","backend","capanel"
}

def cloudflare_bypass(domain):
    print("\n[+] Cloudflare bypass recon")
    print("[*] Enumerating subdomains...\n")
    
    for sub in COMMON_SUBS:
        host = f"{sub}.{domain}"
        try:
            ansewes = dns.resolver.resolve(host, "A")
            for ip in ansewes:
                if is_cloudflare_ip(host):
                    print(f"[GET] {host} -> {ip}")
                else:
                    print(f"[!!!] POSSIBLE REAL SERVER: {host} -> {ip}")
                    
        except:
            pass
        
if __name__ == "__main__":
    cloudflare_bypass("example.com")