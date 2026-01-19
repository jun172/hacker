require "resolv"

domain = ARGV[0]

if domain.nil?
  puts "Usage: ruby dns_recon.rb <domain>"
  exit
end

puts "\n[ DNS Recon ]"
puts "Domain: #{domain}"

# NS Records
puts "\n[ Name Servers ]"
begin
  ns = Resolv::DNS.open { |dns| dns.getresources(domain, Resolv::DNS::Resource::IN::NS) }
  ns.each do |r|
    puts "NS: #{r.name}"
  end
rescue
  puts "NS lookup failed"
end

# A Records
puts "\n[ A Records ]"
begin
  a = Resolv::DNS.open { |dns| dns.getresources(domain, Resolv::DNS::Resource::IN::A) }
  a.each do |r|
    puts "IP: #{r.address}"
  end
rescue
  puts "A record lookup failed"
end

# DNS Provider Guess
puts "\n[ DNS Provider ]"
providers = {
  "cloudflare" => ["cloudflare"],
  "aws route53" => ["awsdns"],
  "google dns" => ["googledomains", "google"],
  "azure" => ["azure", "trafficmanager"],
  "akamai" => ["akam"],
  "fastly" => ["fastly"]
}

ns_names = ns.map(&:name).join(" ").downcase rescue ""

found = false
providers.each do |name, sigs|
  if sigs.any? { |s| ns_names.include?(s) }
    puts "Provider: #{name}"
    found = true
  end
end

puts "Provider: Unknown / Self-hosted" unless found
