import ssl
import socket
from utils import log

def analyze_ssl(domain, port=8081):
    log(f"Analyzing SSL for {domain}")

    context = ssl.create_default_context()

    try:
        with socket.create_connection((domain, port)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

                log(f"Issuer: {cert['issuer']}")
                log(f"Subject: {cert['subject']}")
                log(f"Valid From: {cert['notBefore']}")
                log(f"Valid Until: {cert['notAfter']}")

                return cert

    except Exception as e:
        log(f"SSL error: {e}")
        return None
