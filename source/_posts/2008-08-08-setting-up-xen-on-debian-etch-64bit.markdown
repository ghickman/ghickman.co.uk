---
wordpress_id: 184
layout: post
title: Setting up Xen on Debian etch (64bit)
categories:
 - how-to
---

Today I decided to setup [Xen](http://xen.org) (not the Half-Life world) on a clean Debian installation so I could have a few [VPSes](http://en.wikipedia.org/wiki/Virtual_private_server) to play around with load balancing mySQL, FastCGI and Mongrel. I thought I’d break down the steps I went though to get the basic Xen setup working.

Note: This is by no means a perfect setup, it’s more of a quick way to play around with Xen using a spare PC in the home. If you want more of a production level setup I suggest checking out the Xen website, or Google.

## Step 1. Install Debian (Etch)
Here you just need to setup a standard Debian system, I’m using the 64bit edition of Etch but the process is the same for most Debian releases. I won’t go into detail on how to setup Debian as there are plenty of how-tos out there, for me the normal setup was fine. During the installation I gave the machine **judgement** as the hostname and **gnet.foo** as the domain (you can use whatever) I also unchecked **desktop** from the selectable software menu as I didn’t need/or want a GUI.

##Step 2. Configure Debian ready for Xen
Once you’ve booted and logged into your system you need to install a few applications, but before we do that I tend to remove the CD source from apt-get’s sources.list:

<code>vim /etc/apt/sources.list</code>
<br />
<br />
<code>#comment out the CD line
  #deb cdrom:[Debian...........</code>
<br />
<br />
<code>apt-get update</code>

Now install the packages (remove **vim-full** if you're not using vim):

<code>apt-get install ssh build-essential vim-full</code>

Next we need to configure the server to use a static IP (if you didn't during the installation). I gave my box (**judgement**) a static IP of **192.168.1.10**. Open up the interfaces file:

<code>vim /etc/network/interfaces</code>

Now if you selected DHCP during the installation your file should look similar to this by default (eth2 was my interface, yours might be different):

<code>allow-hotplug eth2
iface eth2 inet dhcp</code>

Change yours to match this (of course change eth2 to match yours and whatever IP you wish to use):

<pre>auto eth
iface eth2 inet static
address 192.168.1.10
netmask 255.255.255.0
network 192.168.1.0
broadcast 192.168.1.255
gateway 192.168.1.1</pre>

Once you've done that you need to restart the networking:

<code>/etc/init.d/networking restart</code>

If all is working then you should be able to ping other computers on your network and they should be able to ping your machine.

If you wish you can continue the rest of the setup via SSH (on windows you can use [Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/)).

Finally just make sure your system is up-to-date before giving it a reboot:

<code>apt-get upgrade
shutdown -r now</code>

##Step 3. Installing Xen
There are two main options when it comes to installing Xen. You can compile it from the source code or simply use apt-get, the latter worked fine for me and is dead simple...to install via apt-get use the following command (bridge-utils is used to setup the network for the virtual machines):

<code>apt-get install xen-linux-system-2.6.18-6-xen-amd64 bridge-utils</code>

The version of Xen kernel might of changed since writing this, try this command to see what's there:

apt-cache search xen-linux
When that has finished installing give the machine a reboot and select Xen kernel from the GRUB menu (for me it became the default option):

<code>shudown -r now</code>

Once the system is back up and logged in (your previous credentials should work) check that you've booted the correct kernel:

<code>uname -r</code>

It should read something like 2.6.18-6-xen-amd64 if not then you've most likely booted the wrong kernel from GRUB.

##Step 4. Creating virtual images or DomU's (the VPSes)
To help with creating, starting, stopping, etc... you need to install xen-tools:

<code>apt-get install xen-tools</code>

Next we need to create the place we want to store the domains (virtual servers), I put mine in /home/xen (xen requires a folder called domains within this folder) so run this command:

<code>mkdir -p /home/xen/domains</code>

Once you've created the location to store the domains you need to edit a few options in Xen's configuration. Start by opening up xend-config.sxp:

<code>vim /etc/xen/xend-config.sxp</code>

and look this for line (around line 70 for me):

{{ 318975 | gist:'gistfile1.txt' }}

and uncomment the **network-script network-bridge** part so it looks like this:

{{ 318975 | gist:'gistfile2.txt' }}

Now we need to setup some defaults as well as the location to store the domains by opening up **xen-tools.conf**:

<code>vim /etc/xen-tools/xen-tools.conf</code>

There are several things to comment out and change here so I'll just list the values I changed in mine:

{{ 318975 | gist:'gistfile3.txt' }}

Restart Xen to make sure the configuration loads correctly:

<code>/etc/init.d/xend restart</code>

You should now be ready to create your first domain. If you're happy with the defaults in the xen-tools.conf file then you can leave a lot of the options out or you can of course put them as arguments of the command, check the man pages for **xen-create-image** for more information:

<code>xen-create-image --hostname=i-am-webial --ip=192.168.1.11 --netmask=255.255.255.0 --gateway=192.168.1.1 --passwd</code>

You should see output of something like this:

{{ 318975 | gist:'gistfile4.txt' }}

Once it's finished you can start your domain by using the following command:

<code>xm create /etc/xen/i-am-webial.cfg</code>

##Extra Stuff
Open a console for the domain:

<code>xm console i-am-webial</code>

you can exit the console by doing **Ctrl + ]**.

To shutdown a domain:

<code>xm shutdown i-am-webial</code>

Increase the RAM of the domain:

<code>vim /etc/xen/i-am-webial.cfg</code>

find and edit memory

<code>memory  = '512' 512</code>

Resize the swap to 1GB (Resize Xen DomU swap):

<code>cd /home/xen/domains/i-am-webial
dd if=/dev/zero of=swap.img bs=1024k count=1024
mkswap swap.img
</code>

Expand the file system by 4 GB (Resize Xen DomU disk)

<code>dd if=/dev/zero bs=1GB count=4 >> disk.img
resize2fs -f disk.img</code>

Hopefully you should now all be setup with basic VPSes, if you need any help with problems please feel free to contact me. You may also leave any feedback/comments you wish below.