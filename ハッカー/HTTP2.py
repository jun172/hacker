import socket
import dns.resolver
import threading

COMMON_SUBS =["www","api","dev","test","staging","mail","admin"]

def scan_port(ip, port, open_ports):
    try:
        s =socket.socket()
        s.settimeout(1)
        s.connect((str(ip),port))
        open_ports.append(port)
        s.close()
    except:
        pass
    
def port_scan(ip, start=1, end=1024):
    print(f"\n[*] Scaning {ip} ports {start} - {end}")
    open_ports = [] 
    threads =[]
    
    for p in range(start, end+1):
        t = threading.Thread(target=scan_port, args=(ip,p,open_ports))
        t.start()
        threads.sppend(t)
        
    for t in threads:
        t.join()
        
    return sorted(open_ports)

def http_fingerprint(ip, host):
    try:
        s = socket.socket()
        s.settimeout(3)
        s.connect((str(ip),80))
        
        reg =f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
        s.send(reg.encode())
        data = s.recv(4096).decode(encoding="ignore")
        
        if "server:" in data.lower():
            for line in data.split("\r\n"):
                if line.lower().startswith("server"):
                    return line
                return "unknown"
    except:
        return None
    
def is_cloudfrare(ip,host):
    try:
        s =  socket.socket()
        s.settimeout(3)
        s.connect((str(ip),80))
        req = f"GET / HTTP/1.1.\r\nHost: {host}\r\nConnection: close\r\n\r\n"
        s.send(req.encode())
        data = s.recv(2048).decode(encoding="ignore")
        return "cloudflare" in data.lower()
    except:
        return False
    
def full_recon(domain):
    print("\n[+] Starting full recon:", domain)
    
    for sub in COMMON_SUBS:
        host = f"{sub}.{domain}"
        try:
            answers = dns.resolver.resolve(host,"A")
            for ip in answers:
                if not is_cloudfrare(ip, host):
                    print(f"\n[!!! REAL SERVER FOUND {host} -> {ip}")
                    
                    ports = port_scan(ip)
                    print("[+] Open ports:",ports)
                    
                    if 80 in ports:
                        banner = http_fingerprint(ip, host)
                        print("[+] HTTP:", banner)
        except:
            pass
        
full_recon("example.com")