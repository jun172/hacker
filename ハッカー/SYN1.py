import socket
import random
import time
import dns.resolver

COMMON_SUBS = ["www","api","dev","direct","origin","backend"]

def find_real_ips(domain):
    ips = set()
    for sub in COMMON_SUBS:
        try:
            host =f"{sub}.{domain}"
            for r in dns.resolver.resolve(host,"A"):
                ips.add(str(r))
        except:
            pass
    return list(ips)

def get_http_banner(host, port=80):
    try:
        sock = socket.create_connection((host, port), timeout=5)
        req= f"GET / HTTP/1.1\r\nHost: {host}\r\nConeection: close\r\n\r\n"
        sock.send(req.encode())
        data = sock.recv(2048).decode(encoding="ignore")
        sock.close()
        
        headers ={}
        for line in data.split("\r\n"):
            if ":" in line:
                k,v = line.split(":",1)
                headers[k.lower()] = v.split()
                
        return headers
    except:
        return {}

def is_cloudflare(headers):
    banner = headers.get("server","").lower()
    return "cloudflare" in banner

def simulate_syn_flood(packets):
    sources = {}
    for _ in range(packets):
        ip = ".".join(str(random.randint(1,254)) for _ in range(4))
        sources[ip] = sources.get(ip,0) + 1
    return sources

def  calculate_score(cloudflare, unique_ips, flood_size):
    socre =0
    if cloudflare:
        socre += 40
    if unique_ips > flood_size * 0.8:
        socre += 30
    if flood_size < 500:
        socre += 30
    return min(socre,100)

def recon(domain):
    print("\n[Recon]")
    print("Target:", domain)
    
    ips = find_real_ips(domain)
    print("\n[ Real IP candidates]")
    for ip in ips:
        print("-",ip)
        
    print("\n[ HTTP Fingerpint]")
    headers = get_http_banner(domain)
    for k,v in headers.items():
        print(k,":",v)
        
    cf = is_cloudflare(headers)
    print("\n[ Cloudflare ]","YES" if cf else "NO")
    
    print("\n[ SYN FLood Simulation]")
    sim = simulate_syn_flood(1000)
    print("Simulated packets:",sum(sim.values()))
    print("unique IPs:",len(sim))
    
    score = calculate_score(cf, len(sim), 1000)
    print("\n[ Resilience Socre]")
    print("Security Ratinng:",score, "/100")
    
if __name__ == "__main__":
    domain = input("Domain:")
    recon(domain)