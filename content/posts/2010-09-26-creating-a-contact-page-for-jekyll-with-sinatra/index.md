---
date: 2010-09-26T00:00:00+00:00
draft: false
title: Creating a Contact Page for Jekyll with Sinatra
tags:
 - Ruby
aliases:
 - /2010/09/26/creating-a-contact-page-for-jekyll-with-sinatra
---

![James Nesbitt in Jekyll](./jekyll.jpg)

Jekyll is a fantastic static site generator with a great little community of modifications around it and I've used it for my own [blog](https://ghickman.co.uk) and [Penderry.com](https://penderry.com). However my biggest problem with it is the lack of a way to deal with a contact form. Of course, this really isn't Jekyll's fault as it's only built to create HTML pages.

Enter Sinatra stage left.

[Sinatra](https://www.sinatrarb.com/) is a rad little web framework, well a micro framework really - in fact it's so small the Hello World app is 5 lines long! It's also perfect for creating a contact form.

To combine the two I needed both of them to display the same layout since I didn't want to have to maintain two. The contact page needed the same layout as the portfolio page, so no sidebar. The easiest way to do this is to plug your Sinatra application into Jekyll's layout mocking up any Jekyll specific objects/variables you need to (like page). I did give using a header and footer includes a go but it broke validation, pah.

My test app is hosted on [Github](https://github.com/ghickman/jekyll_contact) for your viewing pleasure but I'll go through the important parts here too.

```text
!!!
%html
  %head
    %title Jekyll's Contact Form
    %meta{:"http-equiv" => "Content-type", :content => "text/html; charset=utf-8"}
    
    %link{:rel =>'shortcut icon', :href=>'/favicon.ico', :type=>'image/x-icon'}
    %link{:rel=>'stylesheet', :type=>'text/css', :href=>'/stylesheets/master.css', :media=>'screen'}

  %body
    %header
      %h1 Jekyll's Contact From brought to you by Sinatra

    %nav
      %ul
        %li
          %a{:href=>'/', :title=>'Home'} Blog
        %li
          %a{:href=>'http://localhost:4567/contact', :title=>'Contact'} Contact
    
    %section#content== #{content}
      
    %footer
      %div
        %section#jekyll
          Powered by 
          %a{:href=>"http://github.com/richguk/jekyll", :title=>"Jekyll"} Jekyll
        %section#from
          A
          %a{:href=>"http://ghickman.co.uk", :title=>"GHickman Blog"} GHickman
          project
```

Nothing special here, just a bog standard Jekyll layout (well almost, this one is in HAML as I use [RickGuk's Jekyll fork](https://github.com/richguk/jekyll)) with a HAML interpreter bolted on.

The contact page itself is an HTML(5) form that displays some extra bits if we find errors. The test app is done using some HTML 5 specific elements like the email input box but there's no big leaps from HTML 4.

```text
#contact
  %form{:method=>"post"}
    %fieldset
      .input
        %label{:for=>"name"} Name
        %input{:name=>"name", :type=>"text", :id=>"name", :class=>('error' if !@errors[:name].nil?), :required=>{}}
      - if !@errors[:name].nil?
        .error
          %p=@errors[:name]
      
      .input
        %label{:for=>"email"} Email Address
        %input{:name=>"email", :type=>"email", :id=>"email", :class=>('error' if !@errors[:email].nil?), :required=>{}}
      - if !@errors[:email].nil?
        .error
          %p=@errors[:email]
      
      .input
        %label{:for=>"message"} Message
        %textarea{:name=>"message", :id=>"message", :rows=>'5', :class=>('error' if !@errors[:message].nil?), :required=>{}}
      - if !@errors[:message].nil?
        .error
          %p=@errors[:message]
      
      #submit.input
        %input{:type=>"submit", :value=>"Send"}
```

The actual Sinatra application is nice and simple given that we're plugging it into a different layout.

```ruby
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
  @errors[:name] = 'No Anon allowed here.' if params[:name].nil? || params[:name].empty?
  @errors[:email] = 'Sinatra needs an email to send your message from!' if params[:email].nil? || params[:email].empty?
  @errors[:message] = 'No message?! Sounds like heavy breathing on the phone to me.' if params[:message].nil? || params[:message].empty?
  
  if @errors.empty?
    Pony.mail(:to=>'george@ghickman.co.uk', :from=>"#{params[:email]}", :subject=>"Contact Message", :body=>"#{params[:message]}")
    redirect 'http://localhost:4000/index.html'
  else
    contact
  end
end
```

I've started off by setting the views path to Jekyll's source directory so Sinatra knows where to find the contact page and since you can specify a subdirectory the site layout can easily be found later.

The `Page` class is there to emulate the page class that Jekyll uses. Here I've created a title method as my site (what this was originally created for) checks to see what the title of the page is before rendering the sidebar. You can use this method to mock up any of the Jekyll specific objects you wanted, i.e. `site`.

The `contact` method is where the _magic_ really happens. Here we're rending the contact page with Jekyll's layout and passing it our mocked up variables so that Sinatra doesn't freak out when the layout asks for them.

The script is finished off by the get and post methods that both call contact when they want to render a page (making my code nice and DRY). Voila! Jekyll has a contact page!

The last thing to note in the script is the redirect on a successful submission. Since your Sinatra is running on a different port to Jekyll (likely the default 4567) you'll want to redirect back to your Jekyll setup during development. In production this can be changed to `redirect '/index.html'`.

### Setting it up in a Production Environment
Setting this all up in production requires a bit more than Jekyll since you're running a ruby application in the background now. Luckily this is where [Phusion Passenger](https://www.modrails.com/) comes in. You'll need a rack file in your Jekyll root that looks like this:

```ruby
require 'source/_contact'

set :run, false
set :environment, :production

FileUtils.mkdir_p 'log' unless File.exists?('log')
log = File.new("log/sinatra.log", "a")
$stdout.reopen(log)
$stderr.reopen(log)

run Sinatra::Application
```

Don't forget to update the redirect path back from Sinatra to Jekyll, then you're good to go!
