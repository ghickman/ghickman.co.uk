require 'rubygems'
require 'sinatra'
require 'pony'
require 'haml'

set :haml, {:format => :html5}
set :public, File.dirname(__FILE__)
set :views, File.dirname(__FILE__)

# Create the page class and give it a title of Contact for the layout
class Page
  def title
    'Contact'
  end

  def post_page?
    false
  end

  def front_page?
    false
  end
end

def contact
  # create the variables that the layout will expect
  page = Page.new
  content = haml :contact

  # render the contact page using jekyll's layout and with our mock jekyll vars
  haml :contact, :layout=>:'_layouts/default', :locals=>{:page=>page, :content=>content}
end

get '/contact' do
  @errors={}
  contact
end

post '/contact' do
  @errors={}
  @errors[:name] = 'Please enter your name so I know who sent me a message.' if params[:name].nil? || params[:name].empty?
  @errors[:email] = 'How can I can reply without an email address?!' if params[:email].nil? || params[:email].empty?
  @errors[:message] = 'No message?! Sounds like heavy breathing on the phone to me.' if params[:message].nil? || params[:message].empty?
  
  if @errors.empty?
    Pony.mail(:to=>'george@ghickman.co.uk', :from=>"#{params[:email]}", :subject=>"Contact Message from GHickman.co.uk", :body=>"#{params[:message]}")
    redirect '/index.html'
  else
    contact
  end
end
