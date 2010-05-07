---
layout: post
title: Creating the Perfect Torrent Setup
extended: === read more ===
categories:
  - category
  - linux
  - fileserver
  - personal
---

# Deluge
Deluge is an open source BitTorrent client written in Python and comes with a good WebUI and has a nice daemon:interface model running on top of good ol' libtorrent.


## Install Deluge
#### Research Links
* http://dev.deluge-torrent.org/wiki/Installing/Source

There are many prebuilt versions of Deluge for a variety of platforms but I've always had the best results compiling from source so I'll be detailing that here.

First of all grab the source tarball from [here](http://download.deluge-torrent.org/source/) and the libtorrent [source](http://code.google.com/p/libtorrent/downloads/list). At the time of writing I used Deluge 1.2.3 and libtorrent 0.14.9. Download both to your home directory and extract, renaming them to just deluge and libtorrent (from their respective version numbers) to make life a little easier and move the libtorrent directory into the deluge one. This means that when you build Deluge Libtorrent gets built as part of the process - Magic!

=== read more ===

Deluge and libtorrent have a number of dependencies that need to be met before they can be built. But before you can install the main dependencies you'll need a few utilities/packages to let you do so, so run this in your terminal:
<pre>sudo apt-get install build-essential python-dev python-setuptools</pre>

Libtorrent needs the boost libraries, openssl and zlib so run
<pre>sudo apt-get install libboost-dev openssl</pre>

Deluge has a few more dependencies, so I've listed them under the two methods to get them, aren't I nice? (Actually, don't answer that)

#### easy_install
* twisted
* twisted-web
* pyopenssl
* simplejson
* setuptools
* pyxdg
* mako
* pygame
* pygtk

In one easy line:
<pre>sudo easy_install twisted twisted-web pyopenssl simplejson pyxdg mako pygame pygtk</pre>

#### apt-get
* python-notify
* xdg-utils

Easy one-liner:
<pre>sudo apt-get install python-notify xdg-utils</pre>


With dependencies all sorted out change directory to the deluge folder and clean the build environment, just in case something is lurking around:
<pre>python setup.py clean -a</pre>

Build deluge (and libtorrent):
<pre>python setup.py build</pre>

This is the area where you are most likely to get errors so keep an eye on the shell output. I found that most errors were to do missing dependencies or an issue with building libtorrent. I had some luck changing my version of libtorrent, but 9 times out of 10 a dependency is missing.

Next install Deluge with:
<pre>$ sudo python setup.py install</pre>

This places Deluge in your site-packages folder and sets up the appropriate links to the executables in /usr/bin/, these are: deluged, deluge, deluge-gtk, deluge-web and deluge-console.


### Setup Download Folders
I keep all my download folders separate in the following hierarchy under the root of my media share:

* /share/Downloads/complete
* /share/Downloads/incomplete
* /share/Downloads/torrents


## Configure Deluge
Start the daemon by running _deluged_ then start up either the GTK or web UI with _deluge-gtk_ or _deluge-web_.

__Note:__ If you're running the GTK UI you'll need to be either vnc'ed onto the machine or working on it directly when you run deluge-gtk.

### Web UI
Go to the IP address of your server with the port 8112 (the default port), the default password is deluge. You'll be presented with the 'Connection Manager' dialogue box, select the daemon you started earlier (127.0.0.1:58846) and click connect. Click the Preferences button and fill in the Downloads section to point files to be downloaded to incomplete, move completed to complete and autoadd .torrent files from torrents.

### GTK UI
Open Preferences 

# FlexGet
download files
install egg
setup config file
run with -test
run with -v to see what it does
cron job to run every 15/30 minutes.