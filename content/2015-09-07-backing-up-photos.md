Title: Backing Up Photos
Status: draft
Tags: Process

Apple's Photos.app is the primary way I sync my photos between devices.
It does a pretty good job of copying pictures from one device to another.
It even has some really useful extras like photo optimisation for devices which means I can keep 10 years of photos on my phone.
However Apple isn't known for being great at cloud services and syncing isn't a backup (that is to say if iCloud dies I've probably lost all my photos).

There are multiple stages to this, so let's take it from the top:

## Copy Files to NAS
[PhotoSync](https://photosync-app.com/) handles copying photos and videos over to my NAS from iOS.
It provides an impressive array of options for how, what, and when to transfer your media.
I'm using WebDAV via HTTPS and transferring all photos and videos via WiFi.
I've elected to not transfer Live Photos as they create both a photo (the cover image) and a video.

**Note**: I used to handle this step with DropBox but due to how they sync files it killed my internet when coming back from a trip.


## Rename Files Based on EXIF Data


## Fix File Attributes


## Organise


## Backups


I use [Hazel]() to automate the next few steps: fixing orientation, setting filename, and moving to the NAS.

watch /volumes/Pictures/Sync
fix created based on EXIF
fix orientation based on EXIF
change filename to created at datetime
![]()



photos in Photos.app & iCloud service, it's not 100% (typical apple cloud service) but it mostly works. Generally all photos are where I want them and organised how I want them.

Don't trust apple to not lose them all however.

Photos existed pre-Photos.app, iPhone, etc so already used to maintaining them in folders on a file system.

Dropbox allows me to continue doing this by acting as copy mechanism to my desktop

hazel rules
* tidy up: scripts, rotate, rename
* put on fileserver
* periodically put into appropriate folders
* fileserver is backed up
