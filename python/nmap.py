import nmap
nm = nmap.PortScanner()
nm.scan("127.0.0.1", "22-80")

print(nm.csv())