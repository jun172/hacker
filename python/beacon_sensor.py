from bcc import BPF
import time
from collections import defaultdict
from datetime import datetime
import statistics

timestamps = defaultdict(list)

def handler(cpu,data,size):
    event = bpf["events"].event(data)
    key = (event.src,event.dst)
    timestamps[key].append(datetime.now())
    
    if len(timestamps[key]) >= 6:
        intervals = [
            (timestamps[key][i] - timestamps[key][i-1]).total_seconds()
            for i in range(1,len(timestamps[key]))
        ]
        if statistics.pvariance(intervals) < 1.0:
            print(f"[ALERT] C2 Beacon detected {key}")
            timestamps[key].clear()

bpf = BPF(src_file="beacon_ebpf.c")
bpf.attach_kprobe(event="tcp_connect", fn_name="trace_connect")
bpf["events"].open_perf_buffer(handler)

print("[eBPF] Beacon sensor running")

while True:
    bpf.perf_buffer_poll()