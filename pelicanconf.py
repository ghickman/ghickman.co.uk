#!/usr/bin/env python
# -*- coding: utf-8 -*- #

ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

AUTHOR = u'George Hickman'

DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 5

MENUITEMS = (
    ('Archive', '/archives.html'),
    ('Tags', '/tags.html'),
)

RELATIVE_URLS = False

SITENAME = u'ghickman.co.uk'

# Around the web
SOCIAL = (
    ('Twitter', 'https://twitter.com/ghickman'),
    ('GitHub', 'https://github.com/ghickman'),
    ('Amazon', ''),
    ('Bitbucket', ''),
)

SUMMARY_MAX_LENGTH = 50

THEME = 'theme'

TIMEZONE = 'Europe/London'

