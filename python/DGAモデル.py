from bcc import BPF
import socket

def handle(cpu, data, size):
    event = bpf["events"].event(data)
    ip = socket.inet_ntoa(event.src_ip.to_bytes(4,'little'))
    print("DNS from:",ip)
    
bpf = BPF(src_file="dns_ebpf.c")
bpf.attach_kprobe(event="udp_recvmsg", fn_name="dns_monitor")
bpf["events"].open_perf_buffer(handle)

while True:
    bpf.perf_buffer_poll()