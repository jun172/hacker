from scapy.all import sniff, UDP, IP, IPv6, DNS, DNSRR
import time

# LAN上のデバイス情報を保持する辞書
devices = {}

# パケット処理関数
def process_packet(pkt):
    """
    UDP 5353 (mDNS) パケットを監視し、
    Query と Response を処理して devices を更新
    """
    # UDP 5353 のパケットのみ対象
    if UDP in pkt and (pkt[UDP].sport == 5353 or pkt[UDP].dport == 5353):
        # 送信元・宛先IPアドレスを取得（IPv4/IPv6対応）
        src_ip = pkt[IP].src if IP in pkt else (pkt[IPv6].src if IPv6 in pkt else 'unknown')
        dst_ip = pkt[IP].dst if IP in pkt else (pkt[IPv6].dst if IPv6 in pkt else 'unknown')

        # DNS レイヤがある場合のみ処理
        if DNS in pkt:
            dns_layer = pkt[DNS]

            # クエリの処理 (qr==0)
            if dns_layer.qr == 0:
                qname = dns_layer.qd.qname.decode() if dns_layer.qd else ''
                print(f"[QUERY] {src_ip} -> {dst_ip} : {qname}")

            # レスポンスの処理 (qr==1)
            elif dns_layer.qr == 1:
                answers = []
                if dns_layer.an:  # 回答が存在する場合
                    an_count = dns_layer.ancount
                    for i in range(an_count):
                        # 単一回答か複数回答かで分けて処理
                        rr = dns_layer.an[i] if an_count > 1 else dns_layer.an
                        rdata = rr.rdata if hasattr(rr, 'rdata') else None
                        if rdata:
                            answers.append(rdata)
                            # devices 辞書にデバイス情報を追加/更新
                            devices[rdata] = {
                                "ip": rdata,
                                "hostname": rr.rrname.decode() if hasattr(rr, 'rrname') else 'unknown',
                                "last_seen": time.strftime("%H:%M:%S")
                            }
                    # デバイス一覧を表示
                    print(f"[RESPONSE] {src_ip} -> {dst_ip} : answers={answers}")
                    print_devices()

# デバイス一覧表示関数
def print_devices():
    print("\n=== LAN Devices (IPv4/IPv6) ===")
    for ip, info in devices.items():
        print(f"{info['hostname']} ({ip}) last seen: {info['last_seen']}")
    print("==============================\n")

# メイン関数
def main():
    print("Listening on mDNS UDP 5353 (IPv4/IPv6)... Ctrl+C to stop")
    # UDP 5353 にフィルタしてスニッフィング開始
    sniff(filter="udp port 5353", prn=process_packet, store=0)

if __name__ == "__main__":
    main()
