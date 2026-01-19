require 'socket'
require 'time'

DNS_PORT = 1053

RECORDS = {
  "test.local" => "192.168.10.111"
}

query_log = {}

WINDOW = 0.1
THRESHOLD = 0.1

puts "[*] DNS IDS started on UDP #{DNS_PORT}..."

socket = UDPSocket.new
socket.bind("0.0.0.0", DNS_PORT)

loop do
  data, addr = socket.recvfrom(512)
  client_ip = addr[3]
  now = Time.now

  # ===== ドメイン抽出（UTF-8 / ログ用）=====
  idx = 12
  labels = []

  while data.getbyte(idx) != 0
    len = data.getbyte(idx)
    idx += 1
    labels << data.byteslice(idx, len).force_encoding("UTF-8")
    idx += len
  end

  domain = labels.join(".")
  puts "[QUERY] #{client_ip} -> #{domain}"

  # ===== ログ =====
  query_log[client_ip] ||= []
  query_log[client_ip] << { time: now, domain: domain }
  query_log[client_ip].reject! { |q| now - q[:time] > WINDOW }

  uniq_domains = query_log[client_ip].map { |q| q[:domain] }.uniq
  if uniq_domains.size >= THRESHOLD
    puts "🚨 [ALERT] DNS Brute-force detected!"
    puts "    IP: #{client_ip}"
    puts "    Queries: #{uniq_domains.size}/#{WINDOW}s"
  end

  # ===== DNSレスポンス（完全BINARY）=====
  ip = RECORDS[domain]
  next unless ip

  response = "".b
  response << data[0,2]            # TXID
  response << "\x81\x80".b          # flags
  response << data[4,2]             # QDCOUNT
  response << "\x00\x01".b          # ANCOUNT
  response << "\x00\x00\x00\x00".b  # NS / AR
  response << data[12..idx+4]       # QUESTION
  response << "\xC0\x0C".b          # NAME ptr
  response << "\x00\x01\x00\x01".b  # A / IN
  response << "\x00\x00\x00\x3C".b  # TTL
  response << "\x00\x04".b
  response << ip.split(".").map(&:to_i).pack("C*")

  socket.send(response, 0, client_ip, addr[1])
end
