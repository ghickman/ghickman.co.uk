---
layout: post
title: Setup Gitalist with Gitolite on Nginx
extended: === read more ===
categories:
  - git
---
I recently gave [Github's](https://github.com/) paid service a go when my vimrc ended up needing some passwords in it. While I'm a big fan of Github and what it's done for the Git community as a whole I just can't justify paying the £5 a month so I can use my vimrc at home, work and a few servers. Of course the downside is the loss of being able to quickly view code on the web, but as fate would have it Twitter came to my rescue within a couple of days via the sagely [Joel Moss](http://developwithstyle.com/).

<!-- https://twitter.com/joelmoss/status/89637329731461121 -->
<!-- https://twitter.com/joelmoss/status/89637329731461121 --> <style type='text/css'>.bbpBox89637329731461121 {background:url(http://a1.twimg.com/images/themes/theme5/bg.gif) #352726;padding:20px;} p.bbpTweet{background:#fff;padding:10px 12px 10px 12px;margin:0;min-height:48px;color:#000;font-size:18px !important;line-height:22px;-moz-border-radius:5px;-webkit-border-radius:5px} p.bbpTweet span.metadata{display:block;width:100%;clear:both;margin-top:8px;padding-top:12px;height:40px;border-top:1px solid #fff;border-top:1px solid #e6e6e6} p.bbpTweet span.metadata span.author{line-height:19px} p.bbpTweet span.metadata span.author img{float:left;margin:0 7px 0 0px;width:38px;height:38px} p.bbpTweet a:hover{text-decoration:underline}p.bbpTweet span.timestamp{font-size:12px;display:block}</style> <div class='bbpBox89637329731461121'><p class='bbpTweet'>Gitalist - a modern git web viewer <a href="http://j.mp/pJEQtN" rel="nofollow">http://j.mp/pJEQtN</a><span class='timestamp'><a title='Sat Jul 09 10:09:39 +0000 2011' href='https://twitter.com/joelmoss/status/89637329731461121'>less than a minute ago</a> via <a href="http://reederapp.com" rel="nofollow">Reeder</a> <a href='http://twitter.com/intent/favorite?tweet_id=89637329731461121'><img src='http://si0.twimg.com/images/dev/cms/intents/icons/favorite.png' /> Favorite</a> <a href='http://twitter.com/intent/retweet?tweet_id=89637329731461121'><img src='http://si0.twimg.com/images/dev/cms/intents/icons/retweet.png' /> Retweet</a> <a href='http://twitter.com/intent/tweet?in_reply_to=89637329731461121'><img src='http://si0.twimg.com/images/dev/cms/intents/icons/reply.png' /> Reply</a></span><span class='metadata'><span class='author'><a href='http://twitter.com/joelmoss'><img src='http://a2.twimg.com/profile_images/1208340303/pocoyo_avatar_normal.png' /></a><strong><a href='http://twitter.com/joelmoss'>Joel Moss</a></strong><br/>joelmoss</span></span></p></div> <!-- end of tweet -->

Diving into [Gitalist](http://www.gitalist.com/) there were a couple of surprises, least of all it's written in Perl. _Perl?! That's a dead language right? (Unless you're slashdot)_. However playing around with the demo (guys, please up whatever server you're running that on, it's dire) was great, not to mention it looks really slick.

=== read more ===

Gitalist also presented an opportunity to coax my workplace from Mercurial/Bitbucket (Github's corporate pricing has so far been the major reason not to use Git) onto Git, but to do so some sort of access control would be needed, thus Gitolite.

My instructions for this setup are based on setting up on a variety of Ubuntu Server machines: 10.04 plain VM, 10.04 Vagrant and 10.10 real server so they should work reasonably reliably on other Ubuntu versions and child distros.

## Gitolite
[Gitolite](https://github.com/sitaramc/gitolite) is an access control system for Git repositories, a natural successor to [Gitosis](http://scie.nti.st/2007/11/14/hosting-git-repositories-the-easy-and-secure-way), providing fine grained control on a per branch basis. I won't bother going into much detail as there's so much to it and [Sitraramc](http://sitaramc.blogspot.com/) provides a far more comprehensive description on the Github [page](https://github.com/sitaramc/gitolite/wiki/).

I followed the [root install instructions](http://sitaramc.github.com/gitolite/doc/1-INSTALL.html#_root_method) with one caveat when adding the git user, rather than just doing a plain `useradd git` I set some options:

`sudo adduser --system --shell /bin/bash --gecos 'git version control' --group --disabled-password --home /home/git git`

and then run the `su - git` command with `sudo` so you can enter your own password.

Check you can push your projects to the server and you're away!

## Gitalist
### Installation (CPAN)
After some fruitless attempts to install from source and [bootstrap](http://search.cpan.org/dist/Gitalist/lib/Gitalist.pm#BOOTSTRAPPING) I turned to the IRC channel where a noble Internet Hero pointed me at CPAN as the "Way to Go".

First of all CPAN needs a little love. By default it asks you what to do when it finds a dependency it doesn't have.

<!-- http://twitter.com/ghickman/statuses/89982230209904641 -->
<!-- http://twitter.com/ghickman/statuses/89982230209904641 --> <style type='text/css'>.bbpBox89982230209904641 {background:url(http://a1.twimg.com/images/themes/theme2/bg.gif) #C6E2EE;padding:20px;} p.bbpTweet{background:#fff;padding:10px 12px 10px 12px;margin:0;min-height:48px;color:#000;font-size:18px !important;line-height:22px;-moz-border-radius:5px;-webkit-border-radius:5px} p.bbpTweet span.metadata{display:block;width:100%;clear:both;margin-top:8px;padding-top:12px;height:40px;border-top:1px solid #fff;border-top:1px solid #e6e6e6} p.bbpTweet span.metadata span.author{line-height:19px} p.bbpTweet span.metadata span.author img{float:left;margin:0 7px 0 0px;width:38px;height:38px} p.bbpTweet a:hover{text-decoration:underline}p.bbpTweet span.timestamp{font-size:12px;display:block}</style> <div class='bbpBox89982230209904641'><p class='bbpTweet'>"Module X is required, shall I install it?" Well… yea…<span class='timestamp'><a title='Sun Jul 10 09:00:10 +0000 2011' href='http://twitter.com/ghickman/statuses/89982230209904641'>less than a minute ago</a> via <a href="http://itunes.apple.com/us/app/twitter/id409789998?mt=12" rel="nofollow">Twitter for Mac</a> <a href='http://twitter.com/intent/favorite?tweet_id=89982230209904641'><img src='http://si0.twimg.com/images/dev/cms/intents/icons/favorite.png' /> Favorite</a> <a href='http://twitter.com/intent/retweet?tweet_id=89982230209904641'><img src='http://si0.twimg.com/images/dev/cms/intents/icons/retweet.png' /> Retweet</a> <a href='http://twitter.com/intent/tweet?in_reply_to=89982230209904641'><img src='http://si0.twimg.com/images/dev/cms/intents/icons/reply.png' /> Reply</a></span><span class='metadata'><span class='author'><a href='http://twitter.com/ghickman'><img src='http://a0.twimg.com/profile_images/1258522839/gravatar_normal.jpeg' /></a><strong><a href='http://twitter.com/ghickman'>George Hickman</a></strong><br/>ghickman</span></span></p></div> <!-- end of tweet -->

Thankfully it's easy enough to configure CPAN to follow the default options with the `prerequisites_policy` option. Open the CPAN console by running `cpan`.

__Note:__ If it asks you a set of questions instead of giving you a prompt then CPAN wasn't configured when you started. Set them all to default (hit enter) except `prerequisites_policy` which needs to be changed to `follow`. After the proxies section you'll be asked for a [local CPAN mirror](http://www.cpan.org/SITES.html).

To configure type the following into the CPAN console:

`o conf prerequisites_policy follow`

then

`o conf commit`

This sets the `prerequisites_policy` to `follow` the default option for each dependency. Thanks to Mithaldu on #gitalist for helping me out with this.

Back in your favourite flavour of shell it's time for some installations! First up is [YAML](http://yaml.org), which isn't required, but every install complains that it's not there because all the package descriptors seem to be written in it. Installing packages from CPAN is as easy as:

`cpan YAML`

When that's done, it's finally time for Gitalist:

`cpan Gitalist`

Unfortunately some questions still come up, so it's not a completely unattended installation and did take quite a while for me (at least an hour). Default answers again seem fine here.

Test the install by running `sudo gitalist_server.pl` and having a look at `http://<server>:3000/`.

If you get an error about the location of the config then try the methods suggested [here](http://search.cpan.org/dist/Gitalist/lib/Gitalist.pm#FOR_CPAN_INSTALLS). I found none of these worked for me so I grabbed the source from [Github](https://github.com/broquaint/Gitalist) and copied `gitalist.conf` to `/usr/local/share/perl/5.10.x/Gitalist/`.

### Combining with Gitolite
Combining Gitolite and Gitalist is as "simple" as pointing Gitalist at Gitolite's repository directory. Gitolite is running under the `git` user and stores the repositories under `/home/git/repositories/` which won't be accessible to you under another user. The easiest way around this is to run the `gitalist_server.pl` command as the git user like so:

`sudo -u git gitalist_server.pl --repo_dir /home/git/repositories/`

Of course you don't want to be stuck with a command running in the terminal all the time, or having to suffix it with `&` just to have it run in the background so we'll setup [Supervisor](http://supervisord.org/) to handle all of that for us.

#### Supervisor
Supervisor looks after a process and can be configured to perform useful duties like autorestarting and running your process under a different user, both of which we're going to take advantage of. Thankfully supervisor can be installed with ease, like so:

`sudo aptitude install supervisor`

Next you'll need a config file for Gitalist:

`sudo vim /etc/supervisor/conf.d/gitalist.conf`

Paste in the following - setting the path to your gitalist_server.pl to the appropriate place if it's not in the default location.

{{ 1084154 | gist: 'supervisor' }}

Supervisor has a nifty console front end for controlling the processes it looks after. Open it up with `sudo supervisor` and update it to use the Gitalist config with `update`. `status` will show you a list programs you've setup which you can `restart`, `start`, `stop` and `tail` (for program output, `-f` for continuous output). The gitatlist server should now be running under Supervisor, you can check by doing `tail gitalist` Supervisor's console and looking at `http://<server>:3000/`.

#### Nginx
I've connected Nginx and Gitalist via FastCGI which took a bit of fiddling, but I got there in the end. Along the way I toyed around with using Nginx to reverse proxy to the built in Catalyst development server, but had issues with hiding the port number and it felt a bit nasty.

Create yourself a virtual host in nginx's sites-available directory and add the following, changing the server name to something suitable

{{ 1084154 | gist: 'vhost' }}

I've setup the logs under `/var/log/gitalist/` since Gitalist installed via CPAN doesn't really have an install directory as such and that's the logical place. However you'll have to create that directory and make it writable by `www-data` so Nginx has access to it.



Link the virtual host into sites-enabled and test with `sudo nginx -t` to check there are no errors, then reload nginx `sudo /etc/init.d/nginx reload` (or use upstart) and your Gitalist should now be accessible on your domain!

<strong id="fastcgi">A Note on FastCGI:</strong> I originally tried to setup Gitalist and Nginx using FastCGI and went through a lot of pain and suffering over a few evenings. I got pretty close to it working (I had a good half a page of notes for this post) with it only missing styles, images and the ability to display more than the front page before I was pointed at reverse proxying (another hat tip to Mithaldu).



`cpan FCGI::ProcManager` -> needed to run the fcgi bit
build the fastcgi script http://search.cpan.org/dist/Gitalist/lib/Gitalist.pm#RUNNING
setup the config with repo dir
nginx config with fastcgi pass params -> http://wiki.catalystframework.org/wiki/adventcalendararticles/2008/02-catalyst_and_nginx
fastcgi socket

vhost   /etc/nginx/sites-available/git
conf    /usr/local/share/perl/5.10.1/Gitalist/gitalist.conf
fcgi    /usr/local/bin/gitalist_fastcgi.pl
supervsr/etc/supervisor/conf.d/gitalist.conf

sudo gitalist.fcgi -> run the wrapper

-listen for port or socket
-pid for pid
-daemon to daemonise
all require listen

The simplest way to setup Nginx with Gitalist is to reverse proxy connections back to the gitalist_server process. I did play around with setting it up over FastCGI, but that [didn't work out](#fastcgi).
