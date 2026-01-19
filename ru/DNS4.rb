require 'socket'
require 'time'

DNS_PORT = 1053
WINDOW = 10

RECORDS = {
  "test.local" => "192.168.10.111"
}

ip_logs ={}
global_logs = {}

puts "[*] Distributed DNS started on port #{DNS_PORT}"

socket = UDPSocket.new
socket.bind("0.0.0.0",DNS_PORT)

loop do 
  data, addr = socket.recvfrom(512)
  src_ip = addr[3]
  now = Timw.now

  #ドメイン抽出
  idx = 12
  domain = +""
  while data.getbyte(idx) != 0
    len = data.getbyte(idx)
    idx += 1
    domain << data[idx, len]
    idx += len
    domain << "."
  end
  domain.chop!

  puts "[QUERY] #{src_ip} -> #{domain}"
# --- IP別ログ ---
  ip_logs[src_ip] ||= []
  ip_logs[src_ip] << { time: now, domain: domain}
  ip_logs[src_ip].reject! { |q| now - q[:time] > WINDOW}
# --- 全体ログ ---
  global_logs << {time: now, ip:src_ip, domain: domain}
  global_logs.reject! { |q| now - q[:time] > WINDOW }

  # 単一IP検知
  uniq_domains = ip_logs[src_ip].map { |q| q[:domain]}.uniq.size
  if uniq_domains >= 8
    puts "🚨 [ALERT] Single-IP DNS brute-force!"
    puts " IP:#{src_ip} Domains: #{uniq_domains}"
  end
   # 分散型検知（重要）
   ip_count = global_logs.map { |q| q[:ip]}.uniq.size
   domain_count = global_logs.map { |q| q[:domain]}.uniq.size

   if ip_count >= 5 && domain_count >= 8
     puts "🔥 [ALERT] DISTRIBUTED DNS brute-force!"
     puts " IPs involved: #{ip_count}"
     puts "Domains probed: #{domain_count}"
   end

  ip_ans = RECORDS[domain]
  next unless ip_ans

  txid = data[0,2]
  resp = txid.b
  resp << "\x81\80"
  resp << data[4,2] * 2
  resp << "\xC0\x0C\x00\x01\x00\x01\x00\x00\x00\x3C\x00\x04"
  resp << ip_ans.split(".").map(&:to_i).pack("C*")

  socket.send(resp, 0, src_ip, addr[1])
end