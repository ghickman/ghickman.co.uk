---
date: 2011-04-04T00:00:00+00:00
draft: false
title: Using Passenger with RVM and Sinatra
tags:
 - Ruby
aliases:
 - /2011/04/04/passenger-with-rvm-and-sinatra
---
After making the move to [Linode](https://linode.com) (finally!) I had some issues with getting the contact pages on this site and [Penderry](https://penderry.com) up and running. RVM was throwing an error about the sinatra gem missing. A quick scan of the error message and it was obvious that Passenger wasn't using my gemsets.

A bit of googling turned up this little snippet which, when placed in `app/config/`, will tell RVM to use the gemset associated with the folder.

{{< gist ghickman 900934 >}}
