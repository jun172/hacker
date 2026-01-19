require 'socket'

DNS_PORT = 53

RECORDS = {
  "test.local"  => "192.168.10.111",
  "lab.local"   => "192.168.10.111",
  "flask.local" => "192.168.10.111"
}

puts "[*] Ruby DNS Server listening on UDP 53..."

socket = UDPSocket.new
socket.bind("0.0.0.0", DNS_PORT)

loop do
  data, addr = socket.recvfrom(512)
  client_ip = addr[3]

  # ===== ドメイン名抽出 =====
  idx = 12
  name = ""
  while data.getbyte(idx) != 0
    len = data.getbyte(idx)
    idx += 1
    name << data[idx, len]
    idx += len
    name << "."
  end
  name.chop!

  puts "[QUERY] #{client_ip} -> #{name}"

  ip = RECORDS[name]
  next unless ip

  # ===== DNSレスポンス（完全バイナリ）=====
  response = +""
  response.force_encoding("ASCII-8BIT")

  response << data[0,2]            # Transaction ID
  response << "\x81\x80".b         # Flags
  response << data[4,2]            # QDCOUNT
  response << data[4,2]            # ANCOUNT = 1
  response << "\x00\x00\x00\x00".b # NS / AR

  response << data[12..idx+4]      # Question

  response << "\xC0\x0C".b         # Name pointer
  response << "\x00\x01".b         # A record
  response << "\x00\x01".b         # IN
  response << "\x00\x00\x00\x3C".b # TTL
  response << "\x00\x04".b
  response << ip.split(".").map(&:to_i).pack("C*")

  socket.send(response, 0, addr[3], addr[1])
end
