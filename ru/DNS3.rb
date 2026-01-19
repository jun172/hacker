require 'socket'
require 'time'

DNS_PORT = 1053
WINDOW   = 10   # 秒

RECORDS = {
  "test.local" => "192.168.10.111"
}

logs = {}

puts "[*] DNS IDS with Scoring started on UDP #{DNS_PORT}"

socket = UDPSocket.new
socket.bind("0.0.0.0", DNS_PORT)

loop do
  data, addr = socket.recvfrom(512)
  ip  = addr[3]
  now = Time.now

  # --- ドメイン抽出 ---
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

  logs[ip] ||= []
  logs[ip] << { time: now, domain: domain, hit: RECORDS.key?(domain) }
  logs[ip].reject! { |q| now - q[:time] > WINDOW }

  # --- スコア計算 ---
  total     = logs[ip].size
  uniq_dom  = logs[ip].map { |q| q[:domain] }.uniq.size
  nxdomain  = logs[ip].count { |q| !q[:hit] }

  score = 0
  score += [total * 2, 30].min
  score += [uniq_dom * 4, 40].min
  score += (total > 15 ? 20 : 0)
  score += [nxdomain * 2, 10].min

  level =
    case score
    when 0..29  then "🟢 Normal"
    when 30..59 then "🟡 Suspicious"
    when 60..79 then "🟠 Brute-force Likely"
    else             "🔴 Attack Detected"
    end

  puts "[#{ip}] #{domain} | score=#{score} #{level}"

  # --- 正常応答（存在する場合のみ）---
  ip_ans = RECORDS[domain]
  next unless ip_ans

  txid = data[0,2]
  resp = txid.b
  resp << "\x81\x80"
  resp << data[4,2] * 2
  resp << "\x00\x00\x00\x00"
  resp << data[12..idx+4]
  resp << "\xC0\x0C\x00\x01\x00\x01\x00\x00\x00\x3C\x00\x04"
  resp << ip_ans.split(".").map(&:to_i).pack("C*")

  socket.send(resp, 0, ip, addr[1])
end
