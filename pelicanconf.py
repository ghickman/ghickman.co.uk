#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals


ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

AUTHOR = u'George Hickman'

DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 5

FEED_DOMAIN = 'http://ghickman.co.uk'

MENUITEMS = (
    ('Archive', '/archives.html'),
    ('Tags', '/tags.html'),
)

PLUGINS = ('pelican_gist',)

RELATIVE_URLS = False

SITENAME = u'GHickman.co.uk'
SITEURL = ''

# Around the web
SOCIAL = (
    ('twitter', 'https://twitter.com/ghickman'),
    ('github', 'https://github.com/ghickman'),
    ('amazon', 'http://www.amazon.co.uk/registry/wishlist/V6J2GGDHIQ1W'),
    ('stackoverflow', 'http://stackoverflow.com/users/158304/ghickman'),
)

STATIC_PATHS = [
    'static/keybase.txt',
]
EXTRA_PATH_METADATA = {
    'static/keybase.txt': {'path': 'keybase.txt'},
}

SUMMARY_MAX_LENGTH = 50

TEMPLATE_PAGES = {'404.html': '404.html'}

THEME = 'theme'

TIMEZONE = 'Europe/London'
