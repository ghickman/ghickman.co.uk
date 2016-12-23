#!/usr/bin/env python
# -*- coding: utf-8 -*- #
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

AUTHOR = 'George Hickman'

DEFAULT_LANG = 'en'

DEFAULT_METADATA = {
    'status': 'draft',
}

DEFAULT_PAGINATION = 5

PLUGINS = ('pelican_gist',)

RELATIVE_URLS = True

SITENAME = 'GHickman.co.uk'

STATIC_PATHS = [
    'static/keybase.txt',
    'images',
]
EXTRA_PATH_METADATA = {
    'static/keybase.txt': {'path': 'keybase.txt'},
}

SUMMARY_MAX_LENGTH = 50

TEMPLATE_PAGES = {
    '404.html': '404.html',
    'pages/contact.html': 'contact.html',
    'pages/wasgij.html': 'wasgij.html',
}

THEME = 'theme'

TIMEZONE = 'Europe/London'
