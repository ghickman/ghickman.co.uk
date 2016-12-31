#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from collections import OrderedDict

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

WASGIJS = OrderedDict([(
    'Original', [{
        'image': 'http://www.wasgij.co.uk/images/uploads/puzzles/Original_20_Collections_Main.jpg',
        'link': 'http://www.wasgij.co.uk/collections/original/fishy-buisness',
        'name': 'Fishy Business',
        'number': '20',
    }, {
        'image': 'http://www.wasgij.com/images/uploads/puzzles/17_Ballroom_Blushes.jpg',
        'link': 'http://www.wasgij.co.uk/collections/original/ballroom-blushes',
        'name': 'Ballroom Blushes',
        'number': '17',
    }, {
        'image': 'http://www.wasgij.com/images/uploads/puzzles/9_Home_Improvements.jpg',
        'link': 'http://www.wasgij.co.uk/collections/original/home-improvements',
        'name': 'Home Improvements',
        'number': '09',
    }, {
        'image': 'http://www.wasgij.com/images/uploads/puzzles/8_High_Tide.jpg',
        'link': 'http://www.wasgij.co.uk/collections/original/original-8',
        'name': 'High Tide',
        'number': '08',
    }, {
        'image': 'http://www.wasgij.com/images/uploads/puzzles/7_Bear_Necessities.jpg',
        'link': 'http://www.wasgij.co.uk/collections/original/original-7',
        'name': 'Bear Necessities',
        'number': '07',
    }]), (
    'Mystery', [{
        'image': 'http://www.wasgij.com/images/uploads/puzzles/1_Wasgij_Express.jpg',
        'link': 'http://www.wasgij.co.uk/collections/mystery/mystery-1',
        'name': 'Wasgij Express',
        'number': '01'
    }]), (
    'Destiny', [{
        'image': 'http://www.wasgij.com/images/uploads/puzzles/Wasgij-Destiny-13-Collections-Thumbnail-PuzzleImage.png',
        'link': 'http://www.wasgij.co.uk/collections/destiny/commuting-chaos',
        'name': 'Commuting Chaos',
        'number': '13',
    }, {
        'image': 'http://www.wasgij.com/images/uploads/puzzles/12_Market_Mayhem.jpg',
        'link': 'http://www.wasgij.co.uk/collections/destiny/market-mayhem',
        'name': 'Market Mayhem',
        'number': '12',
    }])
])
