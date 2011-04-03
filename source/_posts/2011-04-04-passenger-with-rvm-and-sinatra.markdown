---
layout: post
title: Using Passenger with RVM and Sinatra
extended: === read more ===
categories:
  - coding
  - projects
  - rvm
  - sinatra
---
After making the move to [Linode](http://linode.com) (finally!) I had some issues with getting the contact pages on this site and [Penderry](http://Penderry.com) up and running. RVM was throwing an error about the sinatra gem missing. A quick scan of the error message and it was obvious that Passenger wasn't using my gemsets.

A bit of googling turned up this little snippet which, when placed in `app/config/`, will tell RVM to use the gemset associated with the folder.

{{ 900934 | gist }}
