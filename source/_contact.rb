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
end

post '/contact' do
  @errors={}
  @errors[:name] = 'name error!' if params[:name].nil? || params[:name].empty?
  @errors[:mail] = 'mail error!' if params[:mail].nil? || params[:mail].empty?
  @errors[:message] = 'message error!' if params[:message].nil? || params[:message].empty?
  
  if @errors.empty?
    Pony.mail(:to=>'george@ghickman.co.uk', :from=>"#{params[:mail]}", :subject=>"#{params[:subject]}", :body=>"#{params[:message]}")
    redirect 'http://localhost:4000/index.html'
  else
    puts 'contact'
    haml :contact
  end
end