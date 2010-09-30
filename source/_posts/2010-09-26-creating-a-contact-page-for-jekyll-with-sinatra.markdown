---
layout: post
title: Creating a Contact Page for Jekyll with Sinatra
extended: === read more ===
categories:
  - coding
  - projects
  - ruby
---
<div class="right photo">
    <img src="/images/posts/2010-09-26-creating-a-contact-page-for-jekyll-with-sinatra/jekyll.jpg" width="300" height="169" title="Jekyll" alt="James Nesbitt in Jekyll">
    <p class="photo">
        <a href="http://thetvdb.com/?tab=artistbanners&amp;id=513">Freneticvirus</a>
        <img class="cc" src="/images/cc.png" width="16" height="16" title="Creative Commons Icon" alt="CC">
    </p>
</div>

Jekyll is a fantastic static site generator with a great little community of modifications around it and I've used it for my own [blog](http://ghickman.co.uk) and [Penderry.com](http://penderry.com). However my biggest problem with it is the lack of a way to deal with a contact form. Of course, this really isn't Jekyll's fault as it's only built to create HTML pages.

Enter Sinatra stage left.

[Sinatra](http://www.sinatrarb.com/) is a rad little web framework, well a micro framework really - in fact it's so small the Hello World app is 5 lines long! It's also perfect for creating a contact form.

To combine the two I needed both of them to display the same layout since I didn't want to have to maintain two. The contact page needed the same layout as the portfolio page, so no sidebar. The easiest way to do this is to plug your Sinatra application into Jekyll's layout mocking up any Jekyll specific objects/variables you need to (like page). I did give using a header and footer includes a go but it broke validation, pah.

=== read more ===

My test app is hosted on [Github](http://github.com/ghickman/jekyll_contact) for your viewing pleasure but I'll go through the important parts here too.

{{ 463598 | gist: 'default.haml' }}

Nothing special here, just a bog standard Jekyll layout (well almost, this one is in HAML as I use [RickGuk's Jekyll fork](http://github.com/richguk/jekyll)) with 

The contact page itself is nothing special. An HTML(5) form that displays some extra bits if we find errors. The test app is done using some HTML 5 specific elements like the email input box but there's no big leaps from HTML 4.

{{ 463598 | gist: 'contact.haml' }}

The actual Sinatra application is nice and simple given that we're plugging it into a different layout.

{{ 463598 | gist: '_contact.rb' }}

I've started off by setting the views path to Jekyll's source directory so Sinatra knows where to find the contact page and since you can specify a subdirectory the site layout can easily be found later.

The `Page` class is there to emulate the page class that Jekyll uses. Here I've created a title method as my site (what this was originally created for) checks to see what the title of the page is before rendering the sidebar. You can use this method to mock up any of the Jekyll specific objects you wanted, i.e. `site`.

The `contact` method is where the _magic_ really happens. Here we're rending the contact page with Jekyll's layout and passing it our mocked up variables so that Sinatra doesn't freak out when the layout asks for them.

The script is finished off by the get and post methods that both call contact when they want to render a page (making my code nice and DRY). Voila! Jekyll has a contact page!

The last thing to note in the script is the redirect on a successful submission. Since your Sinatra is running on a different port to Jekyll (likely the default 4567) you'll want to redirect back to your Jekyll setup during development. In production this can be changed to `redirect '/index.html'`.

### Setting it up in a Production Environment
Setting this all up in production requires a bit more than Jekyll since you're running a ruby application in the background now. Luckily this is where [Phusion Passenger](http://www.modrails.com/) comes in. You'll need a rack file in your Jekyll root that looks like this:

{{ 463598 | gist: 'config.ru' }}

Don't forget to update the redirect path back from Sinatra to Jekyll, then you're good to go!