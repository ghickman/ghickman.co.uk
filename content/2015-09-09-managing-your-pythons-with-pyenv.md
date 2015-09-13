Title: Managing Your Pythons with Pyenv
Status: draft
Tags: Python

With the [impending](http://legacy.python.org/dev/peps/pep-0478/) release of Python 3.5 it's that time of year when everyone wants to update their Python 3 version or add another Python to the list of installed versions.

I use [`pyenv`](https://github.com/yyuu/pyenv) to manage my Python versions. It allows you to install various versions of Python (including different interpreters), select the order they appear in your `PATH`, and pin your versions ([just like](http://nvie.com/posts/pin-your-packages/) you do in your `requirements.txt`s, right?!).

As an OS X user I previously used Homebrew for this (and there's already at least [one](http://blog.tim-smith.us/2015/08/python-35-transition/) article explaining how to do this if you prefer to do this). However I found this method fell down as soon as I needed multiple versions of either Python 2 or, more recently, Python 3. It also had the added downside of breaking Tox envs when upgrading the `python3` recipe. `pyenv` gives you control of this, much in the same way Virtualenv did for package versions.

This makes getting Python 3.5 installed a simple matter of telling pyenv to install, then activate it. You can then use it from any tool that looks on the `PATH`, such as Tox.

### Set Up
The [docs](https://github.com/yyuu/pyenv#installation) contain instructions for various installation methods. I use Homebrew: `brew install pyenv`. It will use the `~/.pyenv` directory by default but this is configurable.

Your shell needs to initialise pyenv on start up by running `eval "$(pyenv init -)"` and adding the version [shims](https://github.com/yyuu/pyenv#understanding-shims) to your `PATH`: `export PATH="$HOME/.pyenv/shims:$PATH"`

### Install Some Versions
You can now list the Python versions available with `pyenv install --list` and install a version with `pyenv install <version>`. Unfortunately you can't install multiple versions with the same command. You can list installed versions with `pyenv versions`.

The last thing to do is pick the ordering of your Python versions, for example: `pyenv global 2.7.10 3.4.3 3.3.6`. This means running `python` in your shell will start a Python 2.7.10 shell.

### Pitfalls
Pyenv relies upon `PATH` ordering to make your versions available. However if there are other versions of Python in your `PATH` before pyenv's shims then they will take precedence. A common reason for this is Homebrew installed Python(s) or a stale shell config (test by opening in a new shell).
