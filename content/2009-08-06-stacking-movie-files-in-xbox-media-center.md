Title: Stacking Movie Files in XBox Media Center
Tags: XBMC

I'm the first person to admit that I have some fairly obsessive habits when it comes to making things look nice and neat, more specifically in the media files department. So while playing around with getting my Films folder all neatly into XBox Media Centre (XBMC because I'm lazy and abbreviations FTW) when I found that my films in multiple files weren't stacking properly.

#### What is Stacking and Why Should I Want This Ambrosia of the Gods?!

For those of you unaware of this nifty little feature it lets you take those split film files you have, in formats such as Film (part 1).something and Film (part 2).something and turn them into Film.something with XBMC magic. In technical speak it literally stacks them on top of each other so you see one file instead of many based on the numbering.

Now, I prefer the format Film (1).something to all the others I've seen. I don't need to know it's a part or a disk, this is assumed by the simple action of just having the parenthesis (yes, it means brackets but I'll damned well sound fancy now I have a dictionary at my fingertips!). This of course led to some hacking of XBMC, which as a standard nerd I love doing because it involves hacking at something for ages to make the tiniest little change. This, as it turns out, is actually very easy. The folks over at the XBMC project let you fiddle with all sorts of things using XML files (a personal favourite of mine) to control various eccentricities of your media centre. They also document stuff, so I love them, big time. While perusing [here](http://wiki.xbmc.org/index.php?title=Advancedsettings.xml) I found the `advancedsettings.xml` file that basically lets you do everything, even the dishes in some lovely xml tags. The tag you'll want that lets you play with stacks within this file is the `<moviestacking>` tag where you can place a regex filter. Below is my version for your viewing pleasure:

[gist:id=1255782]

The append section means the rule is appended to the default XBMC rules and the advancedsettings tags are there because, well, it's the advanced settings file. Save the file in your userdata folder, restart XBMC and voila! you'll see the files that you've named in the format I (and [thetvdb.org](http://thetvdb.org) which I use as the default library for [Tv Renamr](http://github.com/ghickman/tvrenamr)) use will stack through what I can only gather is XBMC magic, or regex - which I'm reliably told involves ninjas anyway and they're practically magic. Enjoy!
