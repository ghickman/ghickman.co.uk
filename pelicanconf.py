#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals


ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

AUTHOR = u'George Hickman'

DEFAULT_LANG = u'en'

DEFAULT_METADATA = {
    'status': 'draft',
}

DEFAULT_PAGINATION = 5

FEED_DOMAIN = 'http://ghickman.co.uk'

PLUGINS = ('pelican_gist',)

RELATIVE_URLS = False

SITENAME = u'GHickman.co.uk'
SITEURL = ''

STATIC_PATHS = [
    'static/keybase.txt',
    'images',
]
EXTRA_PATH_METADATA = {
    'static/keybase.txt': {'path': 'keybase.txt'},
}

SUMMARY_MAX_LENGTH = 50

TEMPLATE_PAGES = {'404.html': '404.html'}

THEME = 'theme'

TIMEZONE = 'Europe/London'
