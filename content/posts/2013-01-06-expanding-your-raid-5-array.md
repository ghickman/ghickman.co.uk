---
date: 2013-01-06T00:00:00+00:00
draft: false
title: Expanding your RAID-5 Array
tags:
 - Fileserver
 - RAID
aliases:
 - /2013/01/06/expanding-your-raid-5-array
---
Every so often the time comes around again where I run out of space on my fileserver. Thankfully I'm using RAID-5 so expanding the array is easy enough and the wonderful `mdadm` utility means I can have software RAID so the expansion won't take eons.

Expanding an array with `mdadm` is fairly straightforward:

* Add the new drive to the array
* Expand the array
* Expand the file system

However there are some gotchas along the way that can make the process painful.


## Preparation
Before I start working on any file system I prefer to know that nothing else is trying to access it so I turn off file sharing services as the first order of business.

Then unmount the volume and stop the array:

`sudo umount /mnt/media`

`sudo mdadm --stop /dev/md0`


## Install the New Drive
This has always been the most annoying part I've found with expansions. Quite frequently the drive labels will move around. This is no doubt motherboard related and isn't an issue once you're aware of it! But before then it can be confusing and potentially hazardous.


## Add the New Drive to the Array
Now that the drive is physically in place and you know the label you can get on with the fun stuff and add the drive to your array.

`sudo mdadm --add /dev/md0 /dev/sdf`

Replace `/dev/md0` with your array's volume label `/dev/sdf` with your drive label.

**Note:** Some people prefer to partition drives before adding them to the array. Personally I've never had any issues with unpartitioned devices.


## Expand the Array
Now tell the array to use the new drive:

`sudo mdadm --grow --raid-devices=4 /dev/md0`

**Note:** This part can take anywhere from hours to days, or more, depending on the speed of your machine and the size of disk you're adding to the array.


## Expand the File System
Finally expand your filesystem to fill the new array:

`sudo resize2fs /dev/md0`


## Finishing Touches
The last few bits are reversing what you did before working on the array:

`sudo mount /dev/md0 /mnt/media`

`sudo mdadm --start /dev/md0`

Don't forget to re-enable any services, such as samba or AFP, that you disabled.

