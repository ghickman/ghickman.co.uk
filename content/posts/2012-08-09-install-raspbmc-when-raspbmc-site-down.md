---
date: 2012-08-09T00:00:00+00:00
draft: false
title: How to Install Raspbmc when raspbmc.com is Down
tags:
aliases:
 - /2012/08/09/install-raspbmc-when-raspbmc-site-down
---
`raspbmc.com` down for you? Never fear, the internet has your back.


## Install Script
Copy and paste the python code (starts with `#!/usr/bin/python`) from [here](https://webcache.googleusercontent.com/search?q=cache:https://svn.stmlabs.com/vn/raspbmc/testing/installers/python/install.py) into a file and save it as `install.py`.

Set permissions on it: `chmod +x install.py`.

When you've downloaded the binary (below) run it with `sudo ./install.py`


## Pre-Download the Install Binary
The install script will use `installer.img.gz` if it finds it in the same directory so grab that off the University of Arizona mirror:

```bash
curl -O   https://mirrors.arizona.edu/raspbmc/downloads/bin/ramdistribution/installer.img.gz
```

Now run the install script and you're away!


## A Big Thank You
To [Sam Nazarko](https://twitter.com/SamNazarko) for all his hard working actually making Raspbmc! Also to the various people providing mirror services for the install binary.


## Problems?
It's more than likely that the information above will be out of date pretty soon after I post this entry but don't let that deter you. You can always browse raspbmc.com using Google's Cache by placing any URL from the site after `https://webcache.googleusercontent.com/search?q=cache:`.

You should get automatically routed to a download mirror by going to:

[https://webcache.googleusercontent.com/search?q=cache:https://download.raspbmc.com/](https://mirrors.arizona.edu/raspbmc/downloads/bin/ramdistribution/installer.img.gz)

Then find the install image, it's path should look like

`/downloads/bin/ramdistribution/installer.img.gz`

