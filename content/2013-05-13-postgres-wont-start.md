Title: Postgres Won't Start
Status: published
Tags: Postgres

This problem has caught me out 3 times now so this post is partly just so I don't forget the cause again.


## The Symptoms
Starting or restarting Postgres (with either upstart or init.d) results in a detail-less error, telling you to check your log file. You check the log file… there's nothing useful in there, in fact Postgres might not have even been adding to the logs. The last bit there is what always catches my eye.


## The Cause
The amount of shared memory your OS provides is configured at the kernel level during *installation*. This part is important if you're hosting on VPSs and resizing them as the shared memory value won't change with the amount of RAM you provision.

Postgres has a setting called [shared_buffers](https://www.postgresql.org/docs/9.1/static/runtime-config-resource.html) which configures the amount of shared memory Postgres will consume. The docs suggest using 25% of your total memory value for this setting which is where I got into trouble downsizing VPSs.


## The Solution
There are two places you can fix this problem:

### Postgres
Lower the value of `shared_buffers` so it's within the range of your kernel's `SHMMAX`. You can cat `/proc/sys/kernel/shmmax` to find the value in bytes.

### The Kernel
Edit `/proc/sys/kernel/shmmax` (as root) and change the value it contains to something more suitable for your machine's memory value. Of course this is a brittle solution if you're resizing the machine. However it's a better solution if you wish to tweak the speed of your Postgres installation and are using config management.
