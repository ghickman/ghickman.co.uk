---
layout: post
title: Setup Gitosis with Gitalist on Nginx
extended: === read more ===
categories:
  - git
---
I recently gave [Github's](https://github.com/) paid service a go when my vimrc ended up needing some passwords in it. While I'm a big fan of Github and what it's done for the Git community as a whole I just can't justify paying the £5 a month so I can use my vimrc at home, work and a few servers, especially when I can setup the functionality I was actually using in under five minutes on my own server. The downside to this being the loss of being able to quickly view code viewing on the web. As fate would have it, Twitter came to my rescue within a couple of days via the sagely [Joel Moss](http://developwithstyle.com/).

<!-- https://twitter.com/joelmoss/status/89637329731461121 -->
<!-- https://twitter.com/joelmoss/status/89637329731461121 --> <style type='text/css'>.bbpBox89637329731461121 {background:url(http://a1.twimg.com/images/themes/theme5/bg.gif) #352726;padding:20px;} p.bbpTweet{background:#fff;padding:10px 12px 10px 12px;margin:0;min-height:48px;color:#000;font-size:18px !important;line-height:22px;-moz-border-radius:5px;-webkit-border-radius:5px} p.bbpTweet span.metadata{display:block;width:100%;clear:both;margin-top:8px;padding-top:12px;height:40px;border-top:1px solid #fff;border-top:1px solid #e6e6e6} p.bbpTweet span.metadata span.author{line-height:19px} p.bbpTweet span.metadata span.author img{float:left;margin:0 7px 0 0px;width:38px;height:38px} p.bbpTweet a:hover{text-decoration:underline}p.bbpTweet span.timestamp{font-size:12px;display:block}</style> <div class='bbpBox89637329731461121'><p class='bbpTweet'>Gitalist - a modern git web viewer <a href="http://j.mp/pJEQtN" rel="nofollow">http://j.mp/pJEQtN</a><span class='timestamp'><a title='Sat Jul 09 10:09:39 +0000 2011' href='https://twitter.com/joelmoss/status/89637329731461121'>less than a minute ago</a> via <a href="http://reederapp.com" rel="nofollow">Reeder</a> <a href='http://twitter.com/intent/favorite?tweet_id=89637329731461121'><img src='http://si0.twimg.com/images/dev/cms/intents/icons/favorite.png' /> Favorite</a> <a href='http://twitter.com/intent/retweet?tweet_id=89637329731461121'><img src='http://si0.twimg.com/images/dev/cms/intents/icons/retweet.png' /> Retweet</a> <a href='http://twitter.com/intent/tweet?in_reply_to=89637329731461121'><img src='http://si0.twimg.com/images/dev/cms/intents/icons/reply.png' /> Reply</a></span><span class='metadata'><span class='author'><a href='http://twitter.com/joelmoss'><img src='http://a2.twimg.com/profile_images/1208340303/pocoyo_avatar_normal.png' /></a><strong><a href='http://twitter.com/joelmoss'>Joel Moss</a></strong><br/>joelmoss</span></span></p></div> <!-- end of tweet -->

Diving into [Gitalist](http://www.gitalist.com/) there were a couple of surprises, least of all it's written in Perl. Perl?! That's a dead language right? (Unless you're slashdot). However playing around with the demo (guys, please up whatever server you're running that on, it's dire) was great, not to mention it looks really slick.

=== read more ===

Gitalist also presented an opportunity to coax my workplace from Mercurial/Bitbucket (Github's corporate pricing has so far been the major reason not to use Git) onto Git, but to do so some sort of access control would be needed, thus Gitolite.

My instructions for this setup are based on setting up on a variety of Ubuntu Server machines: 10.04 plain VM, 10.04 Vagrant and 10.10 real server so they should work reasonably reliable on other Ubuntu versions and children distros.

## Gitolite
[Gitolite](https://github.com/sitaramc/gitolite) is an access control system for Git repositories, a natural successor to [Gitosis](http://scie.nti.st/2007/11/14/hosting-git-repositories-the-easy-and-secure-way), providing access control on a per branch basis. I won't bother going into much detail as there's so much to it and [Sitraramc](http://sitaramc.blogspot.com/) provides a far more comprehensive description on the Github [page](https://github.com/sitaramc/gitolite/wiki/).

I followed the [root install instructions](http://sitaramc.github.com/gitolite/doc/1-INSTALL.html#_root_method) with one caveat when adding the git user, rather than just doing a plain `useradd git` I set some options:

`sudo adduser --system --shell /bin/bash --gecos 'git version control' --group --disabled-password --home /home/git git`

and then run the `su - git` command with `sudo` so you can enter your own password.

Now push your projects to the server!

## Gitalist
### Installation (CPAN)
After some fruitless attempts to install from source and [bootstrap](http://search.cpan.org/dist/Gitalist/lib/Gitalist.pm#BOOTSTRAPPING) I turned to the IRC channel where a kindly internet hero pointed me at CPAN as the "Way to Go".

On different systems I found CPAN to be installed in different states. Run `cpan` to see where you need to start from. If you're dropped into a shell straight away then you're probably set to go so jump to [Already Configured](#already-configured), otherwise you should get asked a bunch of questions to set your default options. Set them all to default (hit enter) except `prerequisites_policy` which I changed to `follow`. After the proxies section you'll be asked for a CPAN url mirror, local ones can be found [here](http://www.cpan.org/SITES.html).

<h4 id="already-configured">Already Configured</h4>
Still in the cpan shell type:

`o conf prerequisites_policy follow`

then

`o conf commit`

This sets the `prerequisites_policy` to `follow` the default option, which saves you from hitting enter everytime CPAN discovers a dependency, or a dependency on a dependency and so on...

<!-- http://twitter.com/ghickman/statuses/89982230209904641 -->
<!-- http://twitter.com/ghickman/statuses/89982230209904641 --> <style type='text/css'>.bbpBox89982230209904641 {background:url(http://a1.twimg.com/images/themes/theme2/bg.gif) #C6E2EE;padding:20px;} p.bbpTweet{background:#fff;padding:10px 12px 10px 12px;margin:0;min-height:48px;color:#000;font-size:18px !important;line-height:22px;-moz-border-radius:5px;-webkit-border-radius:5px} p.bbpTweet span.metadata{display:block;width:100%;clear:both;margin-top:8px;padding-top:12px;height:40px;border-top:1px solid #fff;border-top:1px solid #e6e6e6} p.bbpTweet span.metadata span.author{line-height:19px} p.bbpTweet span.metadata span.author img{float:left;margin:0 7px 0 0px;width:38px;height:38px} p.bbpTweet a:hover{text-decoration:underline}p.bbpTweet span.timestamp{font-size:12px;display:block}</style> <div class='bbpBox89982230209904641'><p class='bbpTweet'>"Module X is required, shall I install it?" Well… yea…<span class='timestamp'><a title='Sun Jul 10 09:00:10 +0000 2011' href='http://twitter.com/ghickman/statuses/89982230209904641'>less than a minute ago</a> via <a href="http://itunes.apple.com/us/app/twitter/id409789998?mt=12" rel="nofollow">Twitter for Mac</a> <a href='http://twitter.com/intent/favorite?tweet_id=89982230209904641'><img src='http://si0.twimg.com/images/dev/cms/intents/icons/favorite.png' /> Favorite</a> <a href='http://twitter.com/intent/retweet?tweet_id=89982230209904641'><img src='http://si0.twimg.com/images/dev/cms/intents/icons/retweet.png' /> Retweet</a> <a href='http://twitter.com/intent/tweet?in_reply_to=89982230209904641'><img src='http://si0.twimg.com/images/dev/cms/intents/icons/reply.png' /> Reply</a></span><span class='metadata'><span class='author'><a href='http://twitter.com/ghickman'><img src='http://a0.twimg.com/profile_images/1258522839/gravatar_normal.jpeg' /></a><strong><a href='http://twitter.com/ghickman'>George Hickman</a></strong><br/>ghickman</span></span></p></div> <!-- end of tweet -->

Thanks to Mithaldu on #gitalist for helping me out with this.

Back in your favourite flavour of shell it's time for some installations! First up is [YAML](http://yaml.org) which doesn't seem to be required, but every install complains that it's not there because all the package descriptors seem to be written in it. Installing packages from CPAN is as easy as:

`cpan YAML`

When that's done, it's time for Gitalist finally:

`cpan Gitalist`

Unfortunately some questions still come up, so it's not a completely unattended installation and did take quite a while for me (at least an hour). Default answers again seem fine here.

Test the install by running `sudo gitalist_server.pl` and having a look at `http://<server>:3000/`.

If you get an error about the location of the config then try the methods suggested [here](http://search.cpan.org/dist/Gitalist/lib/Gitalist.pm#FOR_CPAN_INSTALLS). I found none of these worked for me and it was easier to grab the source from [Github](https://github.com/broquaint/Gitalist) and copy `gitalist.conf` to `/usr/local/share/perl/5.10.x/Gitalist/`.

### Combining with Gitolite
Combining Gitolite and Gitalist essentially means pointing Gitalist at the repositories directory of Gitolite. Since this is running under your `git` user it makes life a lot easier if your Gitalist has access to read your Gitolite repositories

Gitosis is running under the `git` user and stores the repositories under `/home/git/repositories/` which won't be accessible to you under a normal user. The easiest way around this is to run the `gitalist_server.pl` command as the git user like so:

`sudo -u git gitalist_server.pl --repo_dir /home/git/repositories/`


`cpan FCGI::ProcManager` -> needed to run the fcgi bit
build the fastcgi script http://search.cpan.org/dist/Gitalist/lib/Gitalist.pm#RUNNING
setup the config with repo dir
nginx config with fastcgi pass params -> http://wiki.catalystframework.org/wiki/adventcalendararticles/2008/02-catalyst_and_nginx
fastcgi socket

vhost   /etc/nginx/sites-available/git
conf    /usr/local/share/perl/5.10.1/Gitalist/gitalist.conf
wrapper /usr/local/bin/gitalist.fcgi
fcgi    /usr/local/bin/gitalist_fastcgi.pl

sudo gitalist.fcgi -> run the wrapper

-listen for port or socket
-pid for pid
-daemon to daemonise
all require listen


Running as www-data user, more correct for the web.


