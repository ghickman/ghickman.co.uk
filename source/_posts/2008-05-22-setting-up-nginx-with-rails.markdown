---
wordpress_id: 18
layout: post
title: Setting up Nginx with Rails
categories:
  - how-to
---
So the other day I decided to switch from using Apache to [Nginx](http://nginx.net/) not because apache isn't any good, far from it. Nginx just uses much less ram and when you're on a fairly small slice, using up more ram just isn't good. I was going to benchmark speed and things between apache and nginx but I forgot to take some readings before stopping the apache service and installing nginx so we'll skip over that idea like the thought never came into my head.

I'll mention a few things I like about nginx first:


1. **It's Russian** - Being Russian means it's build to take some shit.
2. **It uses a lot less memory** - As I said before, not really done much benchmarks so these were some quick figures from 'top' but I had apache running with about 5 instances each using 2-3% of ram even at 2% each that's still 10% of ram being used just for apache... with nginx I appear to have 2 instances running both using 0.2% of ram, so 0.4% in total - which is a nice difference.
3. **Faster page serving** - Nginx is meant to be better at serving static content fast and I've certainly noticed a speed up some with things.

## Installing nginx

I follow pretty much most of these from [slicehost's articles](http://articles.slicehost.com) but I didn't find an article on how to setup the sites-available and sites-enabled type directories for Debian (if you compile from source), so I'll cover that here.

On Debian the package manager contains a rather outdated version of nginx so I'd recommend installing it from the latest source. we'll start by making sure you have all the required library's:

{{ 318944 | gist:'gistfile1.sh' }}

When you're ready you need to obtain the latest source from the nginx website, the latest stable when writing this was 0.6.31.

{{ 318944 | gist:'gistfile3.sh' }}

There are a few options we need to set when compiling from source. I wanted my nginx configuration files in <strong>/etc/nginx</strong> instead of the default, so you may ignore this option (--conf-path) if you prefer the defaults.

We also need to change the location of where nginx puts it's binary files using the <strong>--sbin-path</strong> option because by default this path is set to <strong>/usr/local/nginx</strong> meaning the binary files would be in <strong>/usr/local/nginx/sbin/nginx</strong>
which won't be in our PATH setting, this option will allow the binary files
to be placed where it can be found.

The last option will compile nginx
with the ssl module, so we can have ssl conections.

{{ 318944 | gist:'gistfile4.sh' }}

When the configuration has finish you can compile and install it using make:

{{ 318944 | gist:'gistfile5.sh' }}

This should hopefully of installed nginx into <strong>/usr/local/nginx</strong> and the configuration files into <strong>/etc/nginx</strong>.

When compiling from source we need to make the <strong>/etc/init.d</strong> script ourselves otherwise we'll have no way of starting, stopping and restarting nginx. Slicehost have a script on one of their articles that should be suitable here, so we'll download it and move it to the right directory.

{{ 318944 | gist:'gistfile6.sh' }}

Then finally add it to all the default run levels.

{{ 318944 | gist:'gistfile7.sh' }}

You should now be able to start nginx and browse to it <strong>http://127.0.0.1</strong> (change with your servers IP). If all is working OK you should see a message that says "Welcome to nginx".

{{ 318944 | gist:'gistfile8.sh' }}

<h2>Configuration for Nginx</h2>
The compiled version of nginx doesn't quite have the structure you would have if you'd installed it from apt-get, the package manager sets up a familiar structure to Apache having the <strong>/etc/nginx/sites-available</strong> and <strong>/etc/nginx/sites-enabled </strong>directories, I find this to be a good way of organising all your virtual hosts so lets add that feature.

{{ 318944 | gist:'gistfile9.sh' }}

After we've created the two directories we'll open the nginx.conf file so we can add the following line which will include our virtual host files.

{{ 318944 | gist:'gistfile10.txt' }}

I was unsure the best place to put this so I placed mine after the server {} block, like this.

{{ 318944 | gist:'gistfile2.txt' }}

Once you have done that we are ready to setup our virtual host, for this well proxy all the dynamic content to mongrel and serve all static content using nginx.

{{ 318945 | gist:'gistfile1.sh' }}

You'll want to replace the <strong>site_name</strong> with the name of your site. Into this file paste the following:

{{ 318945 | gist:'gistfile2.txt' }}

Replace <strong>site_name.com</strong> with your domain. You can also rename <strong>give_proxy_a_name</strong> to something else, the name of your site (e.g. 27smiles) should be fine here.

So what does some of that mean? Well the <strong>log</strong> and <strong>root</strong> stuff are pretty straight forward, they define where to put the logs and the what the root folder for the domain is, which in the case of rails will be the public folder within the rails project.

{{ 318945 | gist:'gistfile3.txt' }}

<p style="padding-left: 30px;">This is where you setup the mongrel cluster, for each mongrel server you have running you will need to put a server directive here nginx will then load balance between the servers.</p>

{{ 318945 | gist:'gistfile4.txt' }}

There are 3 IF statements to this bit, the first checks to see if an index.html file exists and if it does then nginx will serve it rather than passing it onto mongrel.

The 2nd IF does pretty much the same but it looks for a html file with the same name as the request. So say you requested <strong>site_name.com/about</strong> it will attempt to find a file called <strong>about.html</strong> in the public folder of the rails project and serve it rather than passing it onto mongrel. This means that if you're using page caching in rails you can skip mongrel for cached pages - very good on performance.

The 3rd IF makes sure the file doesn't exist before passing the request onto mongrel. For example say you requested <strong>site_name.com/images/logo.png</strong> nginx would attempt to locate the file and serve it rather than passing the request on to mongrel, this means you can serve all your static content using nginx instead of mongrel which is much much quicker.

When you've setup your virtual host you need to create a symlink to the sites-enabled folder in order for it to work.

{{ 318945 | gist:'gistfile5.sh' }}

And then finally restart the nginx server.

{{ 318945 | gist:'gistfile6.sh' }}

If all went OK you should be able to browse to your domain name and see your rails project. If not then make sure you created the link to the sites-enabled folder and also that you actually have some mongrel instances running on the IP's you defined (I think you'll get bad gateway messages if it can't find mongrel).

If you need help setting up mongrel head over to <a href="http://articles.slicehost.com">slicehost's article</a> page they have some good articles on how to do it.
<h2>Extra configuration options</h2>
There are a few extra configuration options in nginx that I use on 27smiles; gzip, expiry headers, on another site I also use HTTP authentication. I thought I'd list them here for some people.

If you're looking to setup gzip compression on nginx then add the following.

{{ 318945 | gist:'gistfile7.txt' }}

And finally if you want to password protect domain try this.

{{ 318945 | gist:'gistfile8.txt' }}

If you need any help or have any questions feel free to <a href="http://27smiles.com/contact">contact me</a>.