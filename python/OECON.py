import argparse
import os
import socket
import shlex
import subprocess
import sys
import threading
import asyncio
import json
import ipaddress
import re
from datetime import datetime

VERSION = "2.0"
DEFAULT_TIMEOUT = 1
MAX_THREADS = 100

COMMON_RISKS = {
    21: "FTP exposed",
    23: "Telnet exposed",
    3306: "MySQL exposed",
    6379: "Redis exposed"
}

# ===== 安全なコマンド実行 =====
def run_cmd(cmd):
    try:
        args = shlex.split(cmd)
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return output.decode(errors="ignore")
    except:
        return ""

# ===== Ping =====
def ping_host(host):
    param = "-n" if os.name == "nt" else "-c"
    result = run_cmd(f"ping {param} 1 {host}")
    return "ttl" in result.lower()

# ===== OS推測 =====
def guess_os(host):
    result = run_cmd(f"ping -c 1 {host}")
    match = re.search(r"ttl=(\d+)", result.lower())
    if match:
        ttl = int(match.group(1))
        if ttl <= 64:
            return "Linux/Unix系"
        elif ttl <= 128:
            return "Windows系"
    return "Unknown"

# ===== Banner =====
def grab_banner(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((host, port))
            s.send(b"HEAD / HTTP/1.0\r\n\r\n")
            return s.recv(1024).decode(errors="ignore").strip()
    except:
        return None

# ===== Async Port Scan =====
async def async_scan(host, port):
    try:
        reader, writer = await asyncio.open_connection(host, port)
        writer.close()
        await writer.wait_closed()
        return port
    except:
        return None

async def async_port_scan(host, start, end):
    tasks = [async_scan(host, p) for p in range(start, end+1)]
    results = await asyncio.gather(*tasks)
    return [p for p in results if p]

# ===== JSON保存 =====
def save_json(data):
    filename = f"scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"[+] Saved to {filename}")

# ===== CIDRスキャン =====
def scan_cidr(cidr, start, end):
    network = ipaddress.ip_network(cidr, strict=False)
    for ip in network.hosts():
        print(f"\n=== {ip} ===")
        run_scan(str(ip), start, end)

# ===== メインスキャン処理 =====
def run_scan(host, start, end):
    if not ping_host(host):
        print("Host seems down.")
        return

    print(f"\n[*] Scanning {host} ({start}-{end})")
    open_ports = asyncio.run(async_port_scan(host, start, end))

    results = {
        "host": host,
        "os_guess": guess_os(host),
        "open_ports": []
    }

    for p in open_ports:
        banner = grab_banner(host, p)
        risk = COMMON_RISKS.get(p, None)

        print(f"[+] Port {p} OPEN")
        if banner:
            print(f"    Banner: {banner[:80]}")
        if risk:
            print(f"    Risk: {risk}")

        results["open_ports"].append({
            "port": p,
            "banner": banner,
            "risk": risk
        })

    save_json(results)

# ===== CLI =====
def main():
    print("Recon Framework v", VERSION)

    while True:
        try:
            line = input("recon> ").strip()
        except KeyboardInterrupt:
            print("\nexit")
            break

        if not line:
            continue

        if line == "exit":
            break

        parts = line.split()

        try:
            if parts[0] == "scan" and len(parts) == 4:
                run_scan(parts[1], int(parts[2]), int(parts[3]))

            elif parts[0] == "cidr" and len(parts) == 4:
                scan_cidr(parts[1], int(parts[2]), int(parts[3]))

            elif parts[0] == "sysinfo":
                print(run_cmd("whoami"))
                print(run_cmd("ipconfig" if os.name == "nt" else "ip a"))

            elif parts[0] == "exec" and len(parts) > 1:
                print(run_cmd(" ".join(parts[1:])))

            elif parts[0] == "help":
                print("""
Commands:
 scan <host> <start> <end>
 cidr <network> <start> <end>
 sysinfo
 exec <command>
 exit
""")
            else:
                print("unknown command")

        except Exception as e:
            print("error:", e)

if __name__ == "__main__":
    main()