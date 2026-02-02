import nmap 

nm = nmap.PortScanner()
nm.scan("127.0.0.1","22-80")

for host in nm.all_hosts():
    print("Host:", host)
    for proto in nm[host].all_protocols():
        print("Protocol:", proto)