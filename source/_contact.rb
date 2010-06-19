require 'rubygems'
require 'sinatra'
require 'pony'
require 'haml'

set :public, File.dirname(__FILE__)
set :views, File.dirname(__FILE__) + '/_includes'

helpers do
  def partial(page, options={})
    haml page, options.merge!(:layout => false)
  end
end

get '/contact' do
  @errors={}
  haml :contact
  # ;laksdjfasdfaasdasdadasd
end

post '/contact' do
  @errors={}
  @errors[:name] = 'Please enter your name so I know who sent me a message.' if params[:name].nil? || params[:name].empty?
  @errors[:mail] = 'How can I can reply without an email address?!' if params[:mail].nil? || params[:mail].empty?
  @errors[:message] = 'No message?! Sounds like heavy breathing on the phone to me.' if params[:message].nil? || params[:message].empty?
  
  if @errors.empty?
    Pony.mail(:to=>'george@ghickman.co.uk', :from=>"#{params[:mail]}", :subject=>"#{params[:subject]}", :body=>"#{params[:message]}")
    redirect 'http://localhost:4000/index.html'
  else
    haml :contact
  end
end