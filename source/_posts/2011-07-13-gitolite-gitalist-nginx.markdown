---
layout: post
title: Setup Gitosis with Gitalist on Nginx
extended: === read more ===
categories:
  - git
---
I recently gave [Github's](https://github.com/) paid service a go after my vimrc ended up needing some passwords in it. While I'm a big fan of Github and what it's done for the Git community as a whole I just can't justify paying the £5 a month so I can use my vimrc at home, work and a few servers, especially when I can setup the functionality that service provided me in under five minutes on my own server. Where Github really comes into action is collaborating and publishing code, not to mention the inline editing, which is just awesome, but this was not what I was using it for so away it went. Where I did start to miss Github was for quick code viewing on the web, which is beyond useful when you want to check one file in a project quickly. As fate would have it, Twitter came to my rescue within a couple of days via the sagely [Joel Moss](http://developwithstyle.com/).

https://twitter.com/joelmoss/status/89637329731461121
<!-- https://twitter.com/joelmoss/status/89637329731461121 --> <style type='text/css'>.bbpBox89637329731461121 {background:url(http://a1.twimg.com/images/themes/theme5/bg.gif) #352726;padding:20px;} p.bbpTweet{background:#fff;padding:10px 12px 10px 12px;margin:0;min-height:48px;color:#000;font-size:18px !important;line-height:22px;-moz-border-radius:5px;-webkit-border-radius:5px} p.bbpTweet span.metadata{display:block;width:100%;clear:both;margin-top:8px;padding-top:12px;height:40px;border-top:1px solid #fff;border-top:1px solid #e6e6e6} p.bbpTweet span.metadata span.author{line-height:19px} p.bbpTweet span.metadata span.author img{float:left;margin:0 7px 0 0px;width:38px;height:38px} p.bbpTweet a:hover{text-decoration:underline}p.bbpTweet span.timestamp{font-size:12px;display:block}</style> <div class='bbpBox89637329731461121'><p class='bbpTweet'>Gitalist - a modern git web viewer <a href="http://j.mp/pJEQtN" rel="nofollow">http://j.mp/pJEQtN</a><span class='timestamp'><a title='Sat Jul 09 10:09:39 +0000 2011' href='https://twitter.com/joelmoss/status/89637329731461121'>less than a minute ago</a> via <a href="http://reederapp.com" rel="nofollow">Reeder</a> <a href='http://twitter.com/intent/favorite?tweet_id=89637329731461121'><img src='http://si0.twimg.com/images/dev/cms/intents/icons/favorite.png' /> Favorite</a> <a href='http://twitter.com/intent/retweet?tweet_id=89637329731461121'><img src='http://si0.twimg.com/images/dev/cms/intents/icons/retweet.png' /> Retweet</a> <a href='http://twitter.com/intent/tweet?in_reply_to=89637329731461121'><img src='http://si0.twimg.com/images/dev/cms/intents/icons/reply.png' /> Reply</a></span><span class='metadata'><span class='author'><a href='http://twitter.com/joelmoss'><img src='http://a2.twimg.com/profile_images/1208340303/pocoyo_avatar_normal.png' /></a><strong><a href='http://twitter.com/joelmoss'>Joel Moss</a></strong><br/>joelmoss</span></span></p></div> <!-- end of tweet -->

Diving into [Gitalist](http://www.gitalist.com/) there were a couple of surprises, least of it's written in Perl. Perl?! That's a dead language right? (Unless you're slashdot). However playing around with the demo (guys, please up whatever server you're running that on, it's dire) was great, not to mention it looks really slick.

=== read more ===

Gitalist also presented an opporunity to coax my workplace from Mercurial/Bitbucket (Github's corporate pricing has so far been the major reason not to use Git) onto Git, but to do so some sort of access control would be needed, thus Gitolite.

My instructions are based on setting up an Ubuntu 10.04 LTS machine, so they should work reasonably reliable on other Ubuntu versions and children distros. If you're feeling lucky you might even be able to use them on Debian!

## Gitolite
[Gitolite](https://github.com/sitaramc/gitolite) is an access control system for Git repositories, a natural successor to [Gitosis](http://scie.nti.st/2007/11/14/hosting-git-repositories-the-easy-and-secure-way), providing access control on a per branch basis. I won't bother going into much detail as there's so much to it and [Sitraramc](http://sitaramc.blogspot.com/) provides a far more comprehensive description on the Github [page](https://github.com/sitaramc/gitolite/wiki/).

I followed the [root install instructions](http://sitaramc.github.com/gitolite/doc/1-INSTALL.html#_root_method) with one caveat when adding the git user, rather than just doing a plain `useradd git` I set some options:

`sudo adduser --system --shell /bin/bash --gecos 'git version control' --group --home /home/git git`

and then a password so I could run the `su - git` command:

`sudo passwd git`

## Gitalist
### Installation

http://twitter.com/ghickman/statuses/89982230209904641

<!-- http://twitter.com/ghickman/statuses/89982230209904641 --> <style type='text/css'>.bbpBox89982230209904641 {background:url(http://a1.twimg.com/images/themes/theme2/bg.gif) #C6E2EE;padding:20px;} p.bbpTweet{background:#fff;padding:10px 12px 10px 12px;margin:0;min-height:48px;color:#000;font-size:18px !important;line-height:22px;-moz-border-radius:5px;-webkit-border-radius:5px} p.bbpTweet span.metadata{display:block;width:100%;clear:both;margin-top:8px;padding-top:12px;height:40px;border-top:1px solid #fff;border-top:1px solid #e6e6e6} p.bbpTweet span.metadata span.author{line-height:19px} p.bbpTweet span.metadata span.author img{float:left;margin:0 7px 0 0px;width:38px;height:38px} p.bbpTweet a:hover{text-decoration:underline}p.bbpTweet span.timestamp{font-size:12px;display:block}</style> <div class='bbpBox89982230209904641'><p class='bbpTweet'>"Module X is required, shall I install it?" Well… yea…<span class='timestamp'><a title='Sun Jul 10 09:00:10 +0000 2011' href='http://twitter.com/ghickman/statuses/89982230209904641'>less than a minute ago</a> via <a href="http://itunes.apple.com/us/app/twitter/id409789998?mt=12" rel="nofollow">Twitter for Mac</a> <a href='http://twitter.com/intent/favorite?tweet_id=89982230209904641'><img src='http://si0.twimg.com/images/dev/cms/intents/icons/favorite.png' /> Favorite</a> <a href='http://twitter.com/intent/retweet?tweet_id=89982230209904641'><img src='http://si0.twimg.com/images/dev/cms/intents/icons/retweet.png' /> Retweet</a> <a href='http://twitter.com/intent/tweet?in_reply_to=89982230209904641'><img src='http://si0.twimg.com/images/dev/cms/intents/icons/reply.png' /> Reply</a></span><span class='metadata'><span class='author'><a href='http://twitter.com/ghickman'><img src='http://a0.twimg.com/profile_images/1258522839/gravatar_normal.jpeg' /></a><strong><a href='http://twitter.com/ghickman'>George Hickman</a></strong><br/>ghickman</span></span></p></div> <!-- end of tweet -->

#### CPAN
'First Time Setup'
First time setup - follow the instructions, following defaults. Change `prerequisites_policy` to `follow`.

After the proxies section I was asked for a CPAN url mirror. http://www.cpan.org/SITES.html

`cpan YAML` -> otherwise it complains on every dependency install


Tell cpan to agree to all the default options when asking about new modules to install. Thanks to whoever helped me on IRC with this one, and sorry I don't have a record of your name!

`cpan` to open the shell

`o conf` to show the conf values available -> looking for the `prerequisites_policy`

`o conf prerequisites_policy follow` -> tells cpan to accept the default options when installing.

`o conf commit`

`cpan Gitalist`

X is needed temporarily during building or testing. Do you want to install it permanently? [yes] - Yes

Some questions still come up unfortunately, so it's not a completely unattended installation and did take quite a while for me. I answered yes to everything that came up and it seemed to install fine.

copied the conf from the git checkout because it couldn't find the one that CPAN installed.

Test with `gitalist_server.pl --repo_dir /path/to/repos`

Probably see nothing - see the next section

### Combining Gitosis
Gitosis is running under the `git` user and stores the repositories under `/home/git/repositories/` which won't be accessible to you under a normal user. The easiest way around this is to run the `gitalist_server.pl` command as the git user like so:

`sudo -u git gitalist_server.pl --repo_dir /home/git/repositories/`

test on `http://<server>:3000/


