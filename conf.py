import os

DEBUG = bool(os.environ.get("DEBUG", True))

ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}.html"

AUTHOR = "George Hickman"

DEFAULT_LANG = "en"
DEFAULT_METADATA = {
    "status": "draft",
}
DEFAULT_PAGINATION = 5

DELETE_OUTPUT_DIRECTORY = not DEBUG

# FEEDS, disable all in debug
if DEBUG:
    FEED_ALL_ATOM = None
    CATEGORY_FEED_ATOM = None
    TRANSLATION_FEED_ATOM = None
    AUTHOR_FEED_ATOM = None
    AUTHOR_FEED_RSS = None
else:
    FEED_ALL_ATOM = "feeds/all.atom.xml"
    CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

PATH = "content"

PLUGINS = [
    "pelican_gist",
]

RELATIVE_URLS = DEBUG

SITENAME = "ghickman.co.uk"
SITEURL = "" if DEBUG else "https://ghickman.co.uk"

STATIC_PATHS = [
    "images",
]

SUMMARY_MAX_LENGTH = 50

TIMEZONE = "Europe/London"

TEMPLATE_PAGES = {
    "404.html": "404.html",
    "pages/contact.html": "contact.html",
}

THEME = "theme"
