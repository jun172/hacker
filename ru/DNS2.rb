require 'socket'
require 'securerandom'

DNS_SERVER = "127.0.0.1"
DNS_PORT   = 1053

MAX_SEND   = 30      # ★安全装置（回数）
INTERVAL   = 0.2     # ★速度制限

count = 0
socket = UDPSocket.new

puts "[*] Safe DNS brute-force simulation (loop do)"

loop do
  break if count >= MAX_SEND

  domain = "test#{rand(1000)}.local"

  txid = SecureRandom.random_bytes(2)
  packet = txid + "\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00"

  domain.split(".").each do |part|
    packet << part.length.chr
    packet << part
  end

  packet << "\x00\x00\x01\x00\x01"

  socket.send(packet, 0, DNS_SERVER, DNS_PORT)
  puts "[SEND] #{domain}"

  count += 1
  sleep INTERVAL
end

puts "[*] Simulation finished safely"
