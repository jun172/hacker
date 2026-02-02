import pyshark

cap = pyshark.FileCapture("sample.pcap", display_filter="http")

for packet in cap:
    print(packet.http.host)