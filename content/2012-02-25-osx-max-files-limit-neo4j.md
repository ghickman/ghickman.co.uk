Title: Extending OS X Lion's Maxfiles Limit for Neo4J
Status: published

After upgrading to Neo4j 1.6 today I got this warning when starting the server:

`Detected a limit of 512 for maximum open files.`

A limit of 40000 is suggested instead and a quick look on Google suggests the use of `launchctl limit` or `ulimit -n`. However the results I found were split between how Linux deals with this issue (`ulimit -n`) and pre Lion fixes that involve using `unlimited` as the hard limit (which hasn't worked since Leopard).

Setting a higher limit on lion is fairly simple. Edit `launchd.conf` like so (it might not exist):

`sudo vim /etc/launchd.conf`

Then add this line to it:

`limit maxfiles 1000000 1000000`

This tells Lion to set both the soft and hard limit (in that order) to `1000000`. I picked such a high value to avoid any issues of the same nature in the future.

Make sure you restart afterwards for the changes to take effect.

