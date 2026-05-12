import argparse
import locale
import os
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

# ===== グローバル =====
VERSION = "1.0"
DEFAULT_TIMEOUT = 3

# ===== 安全なシェル実行 =====
def run_cmd(cmd):
    try:
        args = shlex.split(cmd)
        return subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5).decode()
    except subprocess.CalledProcessError as e:
        return e.output.decode()
    except Exception as e:
        return str(e)

# ===== ポートスキャン =====
def scan_port(host, port, results):
    try:
        sock = socket.socket()
        sock.settimeout(DEFAULT_TIMEOUT)
        sock.connect((host, port))
        results.append(port)
        sock.close()
    except:
        pass

def port_scan(host, start, end):
    print(f"\n[*] Scanning {host} ({start}-{end})...\n")
    threads = []
    open_ports = []

    for p in range(start, end + 1):
        t = threading.Thread(target=scan_port, args=(host, p, open_ports))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    for p in sorted(open_ports):
        print(f"[+] Port {p} OPEN")

    print(f"\n[*] Found {len(open_ports)} open ports")

# ===== ローカル情報 =====
def system_info():
    print("\n[*] System Recon\n")
    print(run_cmd("uname -a"))
    print(run_cmd("whoami"))
    print(run_cmd("ifconfig") if os.name != "nt" else run_cmd("ipconfig"))

# ===== バナー =====
def banner():
    print("""
 ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
██╔═══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
██║   ██║█████╗  ██║     ██║   ██║██╔██╗ ██║
██║   ██║██╔══╝  ██║     ██║   ██║██║╚██╗██║
╚██████╔╝███████╗╚██████╗╚██████╔╝██║ ╚████║
 ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
""")

# ===== CLI =====
def main():
    banner()
    print("Recon Framework v", VERSION)
    print("Type 'help' for commands\n")
    
    while True:
        try:
            line = input("recon>").strip()
        except KeyboardInterrupt:
            print("\nexit")
            break
        
        if not line:
            continue
        
        if line == "exit":
            break
        
        if line == "help":
            print("scan <host> <start> <end>")
            print("exec <command>")
            print("clear")
            print("exit")
            continue
        
        if line == "clear":
            os.system("clear")
            continue
        
        parts = line.split()
        
        try:
            if parts[0] == "scan" and len(parts) == 4:
                port_scan(parts[1], int(parts[2]), int(parts[3]))
            elif parts[0] == "sysinfo":
                system_info()
            elif parts[0] == "exec":
                print(run_cmd("".join(parts[1:])))
                
            else:
                print("unknown command")
        except Exception as e:
            print("error:",e)
if __name__ == "__main__": 
    main()