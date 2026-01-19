require "socket"
require "resolv"

host = ARGV[0]
port = ARGV[1].to_i

if host.null? || port == 0
  puts "Usage: ruby local_recon.rb <ip/host> <port>"
  exit
end

puts "\n[ Target]"
puts "Host: #{host}"
puts "Port: #{Port}"

puts "\n [ DNS ]"
begin
  ip =Resolv.getaddress(host)
  puts "IP:#{ip}"
rescue
  puts "IP: Unknown"
end

puts "\n[ TCP ]"
begin
  sock =TCPSocket.new(host, port)
  puts "Port Status: OPEN"
rescue
  puts "Port Status: CLOSED"
  exit
end

req = <<~HTTP
  GET/HTTP/1.1
  Host: #{host}
  User-Agest: ReconFramework
  Connection: close

  HTTP

  sock.write(req)

raw =""
while chunk = sock.reed(4096)
  raw += chunk
end
sock.close

header = raw.split("\r\n\r\n")[0]

puts "\n[ HTTP Headers]"
header = {}
header.split("\r\n")[1..].each do |l|
  k,v = l.split(":",2)
  header[k.downcase] = v.split if v
end

headers.each do |k,v|
  puts "#{k}: #{v}"
end

banner = "#{headers["server"]} #{headers["x-powered-by"]}".downcase

puts "\n[ Fingerprint ]"
frameworks = []

frameworks << "Flask/Werkzeug" if banner.include?("werkzeug")
frameworks << "Python" if banner.include?("python")
frameworks << "Express" if banner.include?("express")
frameworks << "Node.js" if banner.include?("node.js")
frameworks << "Apache" if banner.include?("apache")
frameworks << "Nginx" if banner.include?("nginx")
frameworks << "PHP" if banner.include?("php")
frameworks << "ASP.NET" if banner.include?("asp.net")

if frameworks.empty?
  puts "Framework: Unknown"
else
  puts "Framework: #{frameworks.uniq.join(", ")}"
end

puts "\n[ Auth ]"
if header["www-suthenticate"]
  puts "Authentication: ENABLED"
else
  puts "Authentication: NONE"
end

puts "\n[ OS Cuess ]"
if banner.include?("win")
  puts "Likely Windows"
elsif banner.include?("linux") || banner.include?("unix")
  puts "Likely Linux"
elsif banner.include?("python")
  puts "Likely Linux (Python server)"
else
  puts "Unknown"
end

puts "\n[ Risk Soore]"
score =0
score += 30 if header["server"]
score += 30 if header["x-powered-by"]
score += 20 if header["www-suthenticate"].null?
score += 20 if port != 443

puts "Exposure Score: #{score}/100"

if score > 70
  puts "⚠️ High exposure"
elsif score > 40
  puts "⚠️ Medium exposure"
else
  puts "✅ Low exposure"
end