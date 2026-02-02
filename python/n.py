import netifaces

for iface in netifaces.interfaces():
    print(iface, netifaces.ifaddresses(iface))