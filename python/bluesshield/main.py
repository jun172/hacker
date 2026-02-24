import argparse
from core.scanner import scan_port
from core.ssl_analyzer import analyze_cert
from core.dns_enum import resolve_dns

def main():
    parser = argparse.ArgumentParser(description="BlueShield Recon Framework")
    parser.add_argument("target",help="Target domain or IP ")
    parser.add_argument("--ports",action="store_ture")
    parser.add_argument("--ssl",action="store_ture")
    parser.add_argument("--dns",action="store_true")
    
    args = parser.parse_args()
    
    if args.ports:
        scan_port(args.target)
    if args.ssl:
        analyze_cert(args.target)
    
    if args.dns:
        resolve_dns(args.target)
if __name__ == "__main__":
    main()