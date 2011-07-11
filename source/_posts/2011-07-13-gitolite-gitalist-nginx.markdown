---
layout: post
title: Setup Gitosis with Gitalist on Nginx
extended: === read more ===
categories:
  - git
---

## Gitolite
[Gitolite](https://github.com/sitaramc/gitolite) is an access control system for Git repositories, a natural successor to [Gitosis](), providing access control on a per branch basis.

## Gitalist
### Installation
`cpan YAML` -> otherwise it complains on every dependency install

Tell cpan to agree to all the default options when asking about new modules to install. Thanks to whoever helped me on IRC with this one, and sorry I don't have a record of your name!

`cpan` to open the shell

`o conf` to show the conf values available -> looking for the `prerequisites_policy`

`o conf prerequisites_policy follow` -> tells cpan to accept the default options when installing.

`o conf commit`

`cpan Gitalist`

Some questions still come up unfortunately, so it's not a completely unattended installation and did take quite a while for me. I answered yes to everything that came up and it seemed to install fine.

copied the conf from the git checkout because it couldn't find the one that CPAN installed.

Test with `gitalist_server.pl --repo_dir /path/to/repos`

Probably see nothing - see the next section

### Combining Gitosis
Gitosis is running under the `git` user and stores the repositories under `/home/git/repositories/` which won't be accessible to you under a normal user. The easiest way around this is to run the `gitalist_server.pl` command as the git user like so:

`sudo -u git gitalist_server.pl --repo_dir /home/git/repositories/`

test on `http://<server>:3000/


