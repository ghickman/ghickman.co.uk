Title: Automatically Activate your Dev Environments
Status: published
Tags: Process

I work on a bunch of projects.

Part of switching to a project often involves some setup commands, e.g. adding a directory to my `$PATH`, exporting env vars, or activating a Python `virtualenv`, etc.

Remembering everything I need to do sucks and is error prone, so I automate it where possible.

I use a tool called [direnv](https://direnv.net/) to configure my environment when switching into a directory.
Each of my projects contains a `.envrc` telling direnv what to do when I arrive.
Direnv also handles unloading all these changes when I leave.

Here's an example of my typical Python/Django/Node direnv `.envrc`:

    layout pipenv

    export DEBUG=1
    export KEY=value

    PATH_add ./node_modules/.bin


This handles the following tasks for me:

1. Activate my pipenv controlled virtualenv (direnv ships layouts for most languages).
1. Set some configuration via environment variables.
1. Modify my local `$PATH`, adding node modules' binaries directory to it.

Now I can run Python scripts in the current virtualenv (e.g. `python manage.py runserver`) with the right configuration options or run my npm/yarn scripts without needing to use their direct path.
