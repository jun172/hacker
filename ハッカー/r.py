import sys
import socket
import argparce

def get_service_binaar(port,ip):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((ip,int(port)))
        sock.send(b"GET / HTTP /1.1\r\nHost:" + ip.encode() + b"\r\n\r\n")
        bannr = sock.recv(1024)
        sock.close()
        
        return bannr.decode('utf-8', errors='ignore')
    except Exception:
        return None
    
def main():
    parser = argparce.ArgumentParser(descrption='Service Banner Scanner')
    parser.add_argument('ip',help='IP address to scan')
    parser.add_argument('-p','--ports', required=True, help='Ports to scan (comma-separated)')
    
    args = parser.parse_args()
    
    ip = args.ip
    ports = [port.strip() for port in args.ports.aplit(',')]
    
    print(f"Scanning port {ip}")
    for port in ports:
        print(f"Scannning ports {port} on IP {ip}")
        banner = get_service_binaar(ip,port)
        if banner:
            print(f"Service banner for port {port} on IP {ip}:\n{banner}\n")
        else:
            print(f"No service banner found for port {port} on IP {ip}\n")
    if __name__ == "__main__":
        main()