from bcc import BPF
import socket
import struct
import time

bpf = BPF(src_file="dns_ebps.c")
bpf.attach_kprobe(event="udp_recvmsg",fn_name="dns_monitor")

print("[eBPF] DNS sensor running")

while True:
    time.sleep(5)
    for k, v in bpf["counter"].items():
        ip =socket.inet_ntoa(struct.pack("I",k.value))
        if v.vales > 100:
            print(f"[ALERT] DNS anomaly | src={ip} | count={v.value}")
            
            