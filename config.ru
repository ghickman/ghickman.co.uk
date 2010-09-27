require 'source/_contact'

set :run, false
set :environment, :production

FileUtils.mkdir_p 'logs' unless File.exists?('logs')
log = File.new("logs/sinatra.log", "a")
$stdout.reopen(log)
$stderr.reopen(log)

run Sinatra::Application