import ssl
import socket
from datetime import datetime

def analze_cert(host, port=443):
    context = ssl.create_default_context()
    
    with socket.create_connection((host,port)) as sock:
        with context.wrap_socket(sock,server_hostname=host) as ssock:
            cert = ssock.getpeercert()
            
    print("=== SSL Certificate Analysis ===")
    print("Subject:", cert.get('subject'))
    print("Issuer:", cert.get('issuer'))
    print(" Valid From:",cert.get('notBefore'))
    print("Valid Until:", cert.get('notAfter'))
    
    #有効期限
    expire = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
    if expire < datetime.utcnow():
        print("[ALERT] Certificate expired!")
        
    #SAN確認
    if 'subjectAltName' in cert:
        print("SAN:",cert['subjectAltName'])

analze_cert("example.com")