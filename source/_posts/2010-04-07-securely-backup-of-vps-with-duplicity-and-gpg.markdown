---
layout: post
title: Securely backup your VPS using Duplicity &amp; GnuPG
categories:
  - how-to
extended: === read more ===
---
<div class="figure box left no_margin_top">
	<img src="/images/posts/2010-04-07-securely-backup-of-vps-with-duplicity-and-gpg/3271760209_dba5b4f12c_m.jpg" width="240" height="160">
	<p>
		<img class="cc" src="/images/darkness/creative_commons.png" width="16" height="16" title="Creative Commons image" alt="CC"> 
		<a href="http://www.flickr.com/photos/comedynose/3271760209/">comedynose</a>
	</p>
</div>
It's always a good idea to backup your data; it gives you protection from data loss and hardware failure. If you host sensitive data, or applications for customers, it's a good idea to encrypt the backups, ensuring their secure and can be safely kept just about anywhere.

There are lots of backup scripts, solutions and services around: [Rsync](http://samba.anu.edu.au/rsync/), [s3sync](http://s3sync.net/wiki), [Rdiff-backup](http://rdiff-backup.nongnu.org/), [Jungle Disk](http://www.jungledisk.com/) and [Duplicity](http://www.nongnu.org/duplicity/) being just a few. After trying a few of them I decided to go with Duplicity for my [Linode](http://www.linode.com/?r=00870b85cb89e8747f4319189550b4943bc7483b) VPS; it provided a simple, yet powerful, way of doing encrypted backups.

Duplicity uses librsync and GnuPG to incrementally encrypt archives of files that have changed since the last backup. You can transfer the backups using a whole range of protocols: ftp, imap, rsync, s3 and scp for example - I store backups on my local file server, however, due to the encrypted nature they could easily be stored on something like Amazon's S3.

The MAN pages have more information on the [actions](http://www.nongnu.org/duplicity/duplicity.1.html#toc4), [options](http://www.nongnu.org/duplicity/duplicity.1.html#toc5) and [URL formats](http://www.nongnu.org/duplicity/duplicity.1.html#toc6) for duplicity, it also provides several [examples](http://www.nongnu.org/duplicity/duplicity.1.html#toc3).

=== read more ===

## Installing duplicity and its dependencies
Duplicity is written in python, which needs to be installed if it isn't already (not something covered here). You can install Duplicity via Debian's package manager, but the version is outdated and lacks newer features; to get the latest version it's best to install it from source.

The following dependencies need to be met:

* Python v2.3 or later
* librsync v0.9.6 or later
* GnuPG for encryption
* NcFTP version 3.1.9 or later
* Boto 0.9d or later
* Python development files (python-dev)
* librsync development files (librsync-dev)

Debian users can simply run the following to get all of the required dependencies:

<pre>$ sudo aptitude build-dep duplicity</pre>

Fetch the latest stable release, which as of writing this was 0.6.08b:

<pre>$ mkdir sources<br>$ cd sources<br>$ wget http://code.launchpad.net/duplicity/0.6-series/0.6.08b/+download/duplicity-0.6.08b.tar.gz</pre>

Extract the tarball:

<pre>$ tar xvzf duplicity-0.6.08b.tar.gz<br>$ cd duplicity-0.6.08b</pre>

Finally, install Duplicity:

<pre>$ sudo python setup.py install</pre>

If successful then you should be able to verify by running:

<pre>$ duplicity --version</pre>

<div class="figure box right no_margin_top"><img src="/images/posts/2010-04-07-securely-backup-of-vps-with-duplicity-and-gpg/288491653_0d8802adef_m.jpg" width="240" height="180"><p><img class="cc" src="/images/darkness/creative_commons.png" width="16" height="16" title="Creative Commons image" alt="CC"> <a href="http://www.flickr.com/photos/pong/288491653/">pong</a></p></div>

## Encryption &amp; Keys
Duplicity takes care of the gpg encryption for us, all we have to do is supply a public encryption and signature key. The encryption key is used to protect the data from nosey people, while the signature key is used to ensure the integrity of the backups.

By default, if you omit the signature key, the encryption key is used for signing as well. It's highly recommended to create separate signature and encryption keys; the passphrase for the signature needs to be available in the script, therefore, using the same key for encryption and signing leaves your encrypted files exposed.

On your local machine, not your production server, you can generate the keys with this command:

<pre>$ gpg --gen-key</pre>

You will be given a choice of key types, I normally go with the default - same thing with the key length and expiry. When you're asked to enter a name, you can put what you want, I tend to put the name of the server and which key it is, signature or encryption.

Example of the encryption key generation:

{{355213 | gist: 'gen.txt'}}

Do exactly the same for the signature key, but make sure you use a different passphrase.

Once both keys have been created you need to export and copy the public encryption and private signature keys to the production box; the safest way to do this is SCP/SSH.

To export the keys run the following commands:

<pre>$ gpg --export -a 'Edge Backup Encryption' > edge.enc.pub.gpg<br>$ gpg --export-secret-keys -a 'Edge Backup Signature' > backup.sig.sec.gpg</pre>

Transfer them to the production box:

<pre>$ scp edge.enc.pub.gpg backup.sig.sec.gpg rich@server.com:/tmp</pre>

Import the transferred keys by running the following command (on the production box):

<pre>$ gpg --import /tmp/backup.enc.pub.gpg<br>$ gpg --import-secret-keys /tmp/backup.enc.sec.gpg</pre>

Verify the keys were imported correctly, we also need to note down the key IDs:

<pre>$ gpg --list-keys<br>$ gpg --list-secret-keys</pre>

{{355213 | gist: 'list.txt'}}

The two IDs we're interested in are **5FD0100F** (encryption key) and **7F73FA36** (signature key).

<div class="figure box left no_margin_top"><img src="/images/posts/2010-04-07-securely-backup-of-vps-with-duplicity-and-gpg/2291896028_e54336ab04_m.jpg" width="160" height="240"><p><img class="cc" src="/images/darkness/creative_commons.png" width="16" height="16" title="Creative Commons image" alt="CC"> <a href="http://www.flickr.com/photos/anonymouscollective/2291896028/">anonymouscollective</a></p></div>

## Backup process

I run my backups as root with the scripts running from the root home directory and only readable by root - chmod'ed with 700 (rwx------). I do this for two reasons: one, you need to be able to read all the directories on the server and two, the passphrase needs to be stored in the script.

Before we begin the backups we need to create an exclusion list to ignore certain directories that we don't want to backup. You may include your own directories, or alter the list to better suit your Linux distro.

<pre>$ vim /root/backups/excludelist<br><br># Add the following and save<br>- /sys<br>- /dev<br>- /proc<br>- /tmp<br>- /mnt</pre>

I suggest running the initial backup manually so you can catch any potential errors before automating the process; the initial backup needs to copy everything so expect it to take a while! 

Run the following command, changing the sign and encrypt keys for yours! Time to grab a beer maybe?

<pre>$ duplicity --sign-key '7F73FA36' --encrypt-key '5FD0100F' --exclude-filelist=/root/backups/excludelist / scp://rich@backup_server//mnt/backups/edge/main</pre>

After that has finished confirm the backup ran successfully:

<pre>duplicity collection-status scp://rich@backup_server//mnt/backups/edge/main</pre>

It should list a load of statistics and say something like: _"No orphaned or incomplete backup sets found."_

When you're happy it's all running you can automate the process via a cronjob. Below is the script I use to backup my VPS, note that I dump all the mySQL databases before doing the backup, relying on backups of /var/lib/mysql isn't advised.

{{ 355213 | gist: 'backup.sh' }}

That's it! You should now have secure, fully automated backups of your server. Just make sure you keep your GPG keys safe, I keep mine on a USB pen drive I carry with me.

If you spot any mistakes or want to ask any questions then please, leave a comment.