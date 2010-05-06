---
wordpress_id: 231
layout: post
title: Moved over to Linode from Slicehost
---
Last night and the night before I went though the simple process of moving my websites over from slicehost to Linode. The moved went smoothly and I'm happy with the new provider.

I had been with slicehost for over a year now and they've provided a fantastic service, only ever had my VPS go down once due to a faulty server box I was on. Slicehost have a really nice clean control panel too which was very easy on the eye and simple to manage.

However, all of slicehost's packages are for 64bit systems - no 32bit option offered. I've been looking to head back to 32bit to cut down on the memory consumption in a couple of Merb applications (as you know pointers are 64bit on a 64bit OS and Ruby makes use of pointers quite often). Linode allow you to choose 32bit and because of this I have managed to take my total memory usage of around 420mb down to 218mb with room to breath which has allowed me to drop down to a cheaper package, at least for now.

Linode so far have also been fantastic. The Linode control is a little more 'full' than the Slicehost one but after a few minutes of getting to know your way round it's soon manageable and dare I say nicer, in the way it makes you feel like you're in 'more control' over your server. Linode servers also felt a fair bit quicker, installing stuff seemed snappier and it feels like I get less delay when connecting via SSH - this could be down to the fact I was given a choice of data center and opted for one on the east coast.

On a side note, Linode also offer slighty higher memory, bandwidth and disc space for the same price that slicehost do. For example on the base package of $20 gets you 256mb ram, 100GB monthly bandwidth and 10GB of disc storage with Slicehost compared to the 360mb ram, 200GB bandwidth and 12GB storage you get with Linode.

##Conclusion
So in conclusion I would highly recommend both hosts, I can't comment on Linode up-time wise but so far they've been amazing had my slice within minutes of buying, the server seem quick lots of configuration options right down to which data center you wish to be placed into. Slicehost have been fantastic up-time wise the control is sleek and the packages reasonable.

I would personally recommend Linode if you're trying to save a bit of cash and would like the 32bit option to get that little bit extra memory saving.