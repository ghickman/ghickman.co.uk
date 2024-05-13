---
date: 2011-07-24T00:00:00+00:00
draft: false
title: Setup Gitalist with Gitolite on Nginx
tags:
 - Git
aliases:
 - /2011/07/24/gitolite-gitalist-nginx
---
I recently gave [Github's](https://github.com/) paid service a go when my vimrc ended up needing some passwords in it. While I'm a big fan of Github and what it's done for the Git community as a whole I just can't justify paying the £5 a month so I can use my vimrc at home, work and a few servers. Of course the downside is the loss of being able to quickly view code on the web, but as fate would have it Twitter came to my rescue within a couple of days via the sagely [Joel Moss](https://developwithstyle.com/).

<blockquote class="twitter-tweet"><p>Gitalist - a modern git web viewer https://j.mp/pJEQtN</p>&mdash; Joel Moss (@joelmoss) <a href="https://twitter.com/joelmoss/statuses/89637329731461121">July 9, 2011</a></blockquote>

Diving into [Gitalist](https://www.gitalist.com/) there were a couple of surprises, least of all it's written in Perl. _Perl?! That's a dead language right? (Unless you're slashdot)_. However playing around with the demo (guys, please up whatever server you're running that on, it's dire) was great, not to mention it looks really slick.

Gitalist also presented an opportunity to coax my workplace from Mercurial/Bitbucket (Github's corporate pricing has so far been the major reason not to use Git) onto Git, but to do so some sort of access control would be needed, thus [Gitolite](https://github.com/sitaramc/gitolite).

I've tested these instructions on Ubuntu Server 10.04 so they should work reasonably well on other Ubuntu versions and child distros.

## Gitolite
Gitolite is an access control system for Git repositories, a natural successor to [Gitosis](https://scie.nti.st/2007/11/14/hosting-git-repositories-the-easy-and-secure-way), providing fine grained control on a per branch basis. I won't bother going into much detail as there's so much to it and [Sitraramc](https://sitaramc.blogspot.com/) provides a far more comprehensive description on the Github [page](https://github.com/sitaramc/gitolite/wiki/).

I followed the [root install instructions](https://sitaramc.github.com/gitolite/doc/1-INSTALL.html#_root_method) with a couple of caveats:

I specify the folder locations when running `src/gl-system-install` as it didn't seem to use the default one's listed for me:

`src/gl-system-install /usr/local/bin /usr/local/share/gitolite/conf /usr/local/share/gitolite/hooks`

When adding the git user, rather than just doing a plain `useradd git` I set some options:

`sudo adduser --system --shell /bin/bash --gecos 'git version control' --group --disabled-password --home /home/git git`

and then run the `su - git` command with `sudo` so you can enter your own password.

Check you can push your projects to the server and you're away!

## Gitalist
### Installation (CPAN)
After some fruitless attempts to install from source and [bootstrap](https://search.cpan.org/dist/Gitalist/lib/Gitalist.pm#BOOTSTRAPPING) I turned to the IRC channel where a Big Damn Hero pointed me at CPAN as the "Way to Go".

First of all CPAN needs a little love. By default it asks you what to do when it finds a dependency it doesn't have.

<blockquote class="twitter-tweet"><p>&quot;Module X is required, shall I install it?&quot; Well… yea…</p>&mdash; George Hickman (@ghickman) <a href="https://twitter.com/ghickman/statuses/89982230209904641">July 10, 2011</a></blockquote>

Thankfully it's easy enough to configure CPAN to follow the default options with the `prerequisites_policy` option. Open the CPAN console by running `cpan`.

__Note:__ If CPAN hasn't been configured before you'll be asked if you want it to "configure as much as possible automatically", choose yes then follow the instructions below. However if you do want to go through them manually you'll be asked for a [local CPAN mirror](https://www.cpan.org/SITES.html) after the proxies section.

To configure type the following into the CPAN console:

`o conf prerequisites_policy follow`

then

`o conf commit`

This sets the `prerequisites_policy` to `follow` the default option for each dependency. Thanks to Mithaldu on #gitalist for helping me out and saving hours of tedium.

Finally it's time for some installations! First up is [YAML](https://yaml.org), which isn't required, but every install complains that it's not there because all the package descriptors are written in it. Installing packages from CPAN is as easy as:

`install YAML`

__Note:__ CPAN might update itself at this point, which can take a significant amount of time depending on the power of your machine.

When that's done, it's time for Gitalist:

`install Gitalist`

Unfortunately some questions still come up, so it's not a completely unattended installation and did take quite a while for me (at least an hour). Default answers seem fine though.

Test the install by running `sudo gitalist_server.pl` and having a look at `http://<server>:3000/`.

If you get an error about the location of the config then try the methods suggested [here](https://search.cpan.org/dist/Gitalist/lib/Gitalist.pm#FOR_CPAN_INSTALLS). I found none of these worked for me so I grabbed the source from [Github](https://github.com/broquaint/Gitalist) and copied `gitalist.conf` to `/usr/local/share/perl/5.10.x/Gitalist/`.

Later on we'll setup Gitalist with FastCGI, at which point you'll need Perl's `FCGI::ProcManager` installed as it's the default "Process Manager" for the Gitalist FastCGI script:

`install FCGI::ProcManager`

### Combining with Gitolite
Combining Gitolite and Gitalist is as "simple" as pointing Gitalist at Gitolite's repository directory. Gitolite is running under the `git` user and stores the repositories under `/home/git/repositories/` which won't be accessible to you under another user. The easiest way around this is to run the `gitalist_server.pl` command as the git user like so:

`sudo -u git gitalist_server.pl --repo_dir /home/git/repositories/`

Of course you don't want to be stuck with a command running in the terminal all the time, or having to suffix it with `&` just to have it run in the background so we'll setup [Supervisor](https://supervisord.org/) to handle all of that for us.

#### Supervisor
Supervisor looks after a process and can be configured to perform useful duties like autorestarting and running your process under a different user, both of which we're going to take advantage of. Thankfully supervisor can be installed with ease, like so:

`sudo aptitude install supervisor`

Next you'll need a config file for Gitalist:

`sudo vim /etc/supervisor/conf.d/gitalist.conf`

Paste in the following - setting the path to your gitalist_server.pl to the appropriate place if it's not in the default location.

{{< gist ghickman 1084154 "supervisor" >}}

I've put the socket and pid files in `/var/run/` since Gitalist is installed via CPAN into and [doesn't really](#gitalist-install-dir) have an install directory as such so that's the next logical place. However you'll need to create the gitalist directory there and `chown` it to your `git` user so it can be written to by the FastCGI script (which is now running under the `git` user). The `--nproc` switch tells the script how many processes to run, like Nginx's workers directive. To see all the options run `/usr/local/bin/gitalist_fastcgi.pl --help` in your terminal.

Open up Supervisor's nifty console with `sudo supervisorctl` and tell it to `update` so that it uses your Gitalist config (you'll need to do this after any updates to a configuration file). `status` will show you a list programs you've setup which you can `start`, `stop`, `restart` and `tail` (for program output, with `-f` for continuous output). The gitatlist server should now be running under Supervisor, check with the `tail gitalist` to make sure there are no errors in the output.

#### Gitalist Config
Since we're using FastCGI to pass requests from Nginx through to Gitalist we'll use the Gitalist config file (you can't pass Gitalist configuration values to the FastCGI script). Open it up in your favourite editor:

`sudo vim /usr/local/share/perl/5.10.1/Gitalist/gitalist.conf`

and set the `repo_dir` option to `/home/git/repositories/`:

{{< gist ghickman 1084154 "gitalist.conf" >}}

#### Nginx
Create yourself a virtual host in nginx's sites-available directory and add the following, changing the server name to something suitable:

{{< gist ghickman 1084154 "vhost" >}}

I've setup the logs under `/var/log/gitalist/` for the same reason as the socket and the pid files, again you'll have to create that directory but make it writable by `www-data` so Nginx has access to it.

Link the virtual host into sites-enabled and test with `sudo nginx -t` to check there are no errors, then reload nginx `sudo /etc/init.d/nginx reload` (or use upstart) and your Gitalist should now be accessible on your domain!

## Notes
#### FastCGI vs. Reverse Proxying

While getting FastCGI setup I toyed with Nginx as a reverse proxy to the one or more instances of the Catalyst development server, but had issues with hiding the port number and it felt a bit wrong to use a development server in production.

<h4 id="gitalist-install-dir">Gitalist Install Directory</h4>

Having installed Gitalist via CPAN it lives under `/usr/local/share/perl/5.10.1/Gitalist/` which seems a bad place to store a socket file, a pid file or any logs which is why I chose to put them all under `/var/`.

## Extra Reading
* [Catalyst and Nginx (Catalyst Docs)](https://wiki.catalystframework.org/wiki/adventcalendararticles/2008/02-catalyst_and_nginx)
* [Gitalist, FastCGI and Nginx (Catalyst Docs on CPAN)](https://search.cpan.org/~bobtfish/Catalyst-Runtime-5.80032/lib/Catalyst/Engine/FastCGI.pm#nginx)
* [Catalyst Standalone Server (Gitalist Docs on CPAN)](https://search.cpan.org/dist/Catalyst-Manual/lib/Catalyst/Manual/Cookbook.pod#Standalone_server_mode)

<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
