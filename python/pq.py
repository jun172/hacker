import psutil
net = psutil.net_io_counters()
print(net.bytes_sent, net.bytes_recv)
