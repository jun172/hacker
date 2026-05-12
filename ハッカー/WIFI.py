import pyshark

capture = pyshark.LiveCapture(
    interface='en0',
    bpf_filter='arp'
)

print("ARP sniffing... Ctrl+C to stop")

for packet in capture.sniff_continuously():
    try:
        arp = packet.arp
        print(
            f"ARP {arp.opcode} "
            f"{arp.src_proto_ipv4} ({arp.src_hw_mac}) "
            f"-> {arp.dst_proto_ipv4}"
        )
    except AttributeError:
        pass
