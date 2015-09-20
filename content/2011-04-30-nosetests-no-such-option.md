Title: Nose Tests - no such option
Status: published
Tags: Python, Testing

Some time ago now I added proper command line options to [Tv Renamr](http://github.com/ghickman/tvrenamr), followed shortly by a test suite with Python's [Nose](http://somethingaboutorange.com/mrl/projects/nose/1.0.0/). Along the way I ran into a bug that has frustrated me for a long long time, until today when I finally found a work around - hooray, go me!

The bug is hardly a game stopper as it only affects the UI candy on my tests. Simply put, I couldn't use options with nose. Every time I did, an error was thrown saying no such option existed for nose while displaying the usage string for tvr:

![](/images/nose-tests.png)

This initially prompted me to split the front end script's options into a [separate](https://github.com/ghickman/tvrenamr/commit/b77e16d97f7712de38625381e194d43e090a3fde) file which didn't solve the issue, but did wonders for cleaning up the codebase.

This seems to have affected at least [one](http://ionelmc.wordpress.com/2008/04/24/setuptools-nosetests-oddness/) other person, whose post finally gave me the lightbulb today. [Ionel](http://ionelmc.wordpress.com/) mentions in his post "Luckily, setuptools has aliases for commands and instead of" and a snippet of a config file. It's only taken me a couple of years (I've tried to fix this at least 3 times now and always drawn blanks sadly) to realise that he was using a config file. A quick google for the appropriate section in the [nose docs](http://somethingaboutorange.com/mrl/projects/nose/1.0.0/man.html#configuration) turned up enough information to construct a useful rc file:

[gist:id=949702,file=.noserc]

And so I finally have my lovely coloured output, with [Growl](https://bitbucket.org/crankycoder/nosegrowl) integration, back. This is shaping up to be quite the productive weekend.
