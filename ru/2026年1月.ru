#!/usr/bin/env ruby
# Recon + Cloudflare bypass + HTTP Fingerprint + SYN Simulation + Traffic Analysis + Resilience Score
# White-hat Security Research Tool

require 'resolv'
require 'net/http'
require 'open3'

TARGET = ARGV[0] || "http://192.168.10.111:8081"
PCAP   = ARGV[1]   # optional traffic capture

COMMON_SUBS = %w[
  www api dev test staging mail direct backend admin old
]

# ----------------------------
# DNS Recon
# ----------------------------
def resolve(host)
  Resolv.getaddresses(host)
rescue
  []
end

# ----------------------------
# Cloudflare Detection
# ----------------------------
def cloudflare?(host)
  res = Net::HTTP.get_response(URI("http://#{host}"))
  res['server']&.downcase&.include?("cloudflare")
rescue
  false
end

# ----------------------------
# HTTP Fingerprint
# ----------------------------
def fingerprint(host)
  res = Net::HTTP.get_response(URI("http://#{host}"))
  {
    server: res['server'] || "unknown",
    powered: res['x-powered-by'] || "unknown"
  }
rescue
  { server: "unknown", powered: "unknown" }
end

# ----------------------------
# Virtual SYN Flood Simulation
# ----------------------------
def syn_simulation(requests, ips)
  syn = requests
  ack = (requests * 0.25).to_i   # 25% handshake success
  { syn: syn, ack: ack, ips: ips }
end

# ----------------------------
# Real Traffic Analysis (pcap)
# ----------------------------
def analyze_pcap(file)
  syn = `tshark -r #{file} -Y "tcp.flags.syn==1 && tcp.flags.ack==0" 2>/dev/null | wc -l`.to_i
  ack = `tshark -r #{file} -Y "tcp.flags.ack==1" 2>/dev/null | wc -l`.to_i
  ips = `tshark -r #{file} -T fields -e ip.src 2>/dev/null | sort | uniq | wc -l`.to_i

  { syn: syn, ack: ack, ips: ips }
end

# ----------------------------
# Resilience Score
# ----------------------------
def score(data)
  score = 100
  score -= 40 if data[:syn] > 200
  score -= 30 if data[:ips] > 50
  score -= 30 if data[:ack].to_f / [data[:syn],1].max < 0.3
  score.clamp(0,100)
end

puts "\n[ Recon ] Subdomain enumeration"
real_hosts = []

COMMON_SUBS.each do |sub|
  host = "#{sub}.#{TARGET}"
  resolve(host).each do |ip|
    if cloudflare?(host)
      puts "[CF]  #{host} -> #{ip}"
    else
      puts "[REAL] #{host} -> #{ip}"
      real_hosts << host
    end
  end
end

puts "\n[ HTTP Fingerprints ]"
real_hosts.each do |h|
  fp = fingerprint(h)
  puts "#{h.ljust(20)} | Server: #{fp[:server]} | X-Powered-By: #{fp[:powered]}"
end

puts "\n[ SYN Flood Simulation ]"
sim = syn_simulation(500, 120)
puts "Virtual SYN: #{sim[:syn]}"
puts "Virtual ACK: #{sim[:ack]}"
puts "Virtual IPs: #{sim[:ips]}"

if PCAP
  puts "\n[ Real Traffic Detection ]"
  real = analyze_pcap(PCAP)
  puts "Observed SYN: #{real[:syn]}"
  puts "Observed ACK: #{real[:ack]}"
  puts "Unique IPs: #{real[:ips]}"

  puts "\n[ Resilience Score ]"
  puts "DDoS Resistance: #{score(real)}/100"
else
  puts "\n[ Resilience Score (Simulation) ]"
  puts "Estimated Resistance: #{score(sim)}/100"
end
