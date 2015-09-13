Title: TV Renamr - Finally
Slug: tv-renamr-finally
Status: published
Tags: Python, TV Renamr

For the last few years I've always wanted to create a program that renamed the TV files I had into the nice neat format that I seem to spend so much of my spare time doing manually. Well, on my birthday I decided to take the plunge, stop talking about it and get my arse in gear. On that day, 22 years after my mother labouriously gave birth to me Tv Renamr was created in what I have no doubt was a far less spectacular fashion than the miracle of child birth. I started off with a short script in Python with various bits taken de facto from the internet. It sort of worked, as long as your files were in the correct format to begin with, which was a pretty narrow groove for your files to be. Which of course mine weren't.

*Fast forward to a few months later and roughly the present day...*

After the joy of final exams and the stress of moving back in with my parents and some random hacking away at my code I've ended up with a nicely object oriented Python API that takes a few formats and gives the user a variety of ways to rename TV files. I've even had a crash course in python testing, something which has recently proved invaluable to being able to dip in and out of the project as I please. The passing in of files and information is now pretty much complete, a user can choose the series name, the season number, the episode number (if you're doing a single file) and even specify a regex expression which is always useful if like me you want to make sure your Stargate SG-1 rips are perfect. I even have tests to back up my work, which in a personal project is a first for me, but damn is it awesome to see that growl popup with a green tick. It's like a giant thumbs up!

Next on the agenda is customising the output. The more important part of this is letting the user specify how to deal with characters that aren't supported by their file system. While Python already deals with this, I want to give the user the choice to specify what characters they want replaced and how. Then it's onto the output format, which I'm ignoring for now, because it sounds big and I haven't even got a test file ready for it yet *eep*.

This project has taught me a few things about myself and coding along the way - coding stuff you're really interested in is hellishly fun (I've literally lost days to this project without even noticing) and doing it in a language you've barely tried before is a massive confidence boost to your skill level.

The project is of course hosted on my [github page](http://github.com/ghickman/tvrenamr/tree/master) where you can download it or clone it to your neat little heart's content. If you find any bugs or problems, please add an issue on github, dm/@ me on [twitter](http://twitter.com/ghickman) or email me on george [at] ghickman -dot- co -dot- uk.
