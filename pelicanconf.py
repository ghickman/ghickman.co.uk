#!/usr/bin/env python
# -*- coding: utf-8 -*- #

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

PAGE_DIR = 'pages'

RELATIVE_URLS = False

SITENAME = u'GHickman.co.uk'

# Around the web
SOCIAL = (
    ('twitter', 'https://twitter.com/ghickman'),
    ('gitHub', 'https://github.com/ghickman'),
    ('amazon', 'http://www.amazon.co.uk/registry/wishlist/V6J2GGDHIQ1W'),
    ('stackoverflow', 'http://stackoverflow.com/users/158304/ghickman'),
)

SUMMARY_MAX_LENGTH = 50

THEME = 'theme'

TIMEZONE = 'Europe/London'

