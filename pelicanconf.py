#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Alexandre Chabot-Leclerc'
SITENAME = 'AlexChabot.net'
# SITESUBTITLE = ""
SITEURL = 'http://localhost:8000'
# ARTICLE_PATHS = []

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

LOAD_CONTENT_CACHE = False

# Do not delete output folder because it has the git repo for serving on
# Github.
DELETE_OUTPUT_DIRECTORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


# FORMATTING FOR URLS
# Configure Pelican to output Clean URLs
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
PAGE_URL =  ''
CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"


# Show full articles on homepage
SUMMARY_MAX_LENGTH = False

# Generate yearly archive
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/index.html'


# Social widget & menus
MENUITEMS = (
    ('About', '/about'),
    ('Projects', '/projects'),
    ('Archives', '/Archives')
)
TWITTER_USERNAME = "AlexChabotL"
GITHUB_USERNAME = 'achabotl'

DEFAULT_PAGINATION = 4
# first page to just be /, and the second (and subsequent) pages to be /page/2/
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME='theme'
PYGMENTS_STYLE = 'friendly'
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = False
HIDE_SIDEBAR = True
CC_LICENSE = "CC-BY"

TYPOGRIFY = True

OUTPUT_SOURCES = True

# EXTRA_PATH_METADATA = {
#     'extra/CNAME': {'path': 'CNAME'},
#     'extra/README.markdown': {'path': 'README.markdown'},
#     'extra/favicon.ico': {'path': 'favicon.ico'},
#     'extra/favicon.png': {'path': 'favicon.png'},
#     'extra/404.html': {'path': '404.html'},
#     'extra/robots.txt': {'path': 'robots.txt'},
#     'extra/google3f40dbd543a603fa.html': {'path': 'google3f40dbd543a603fa.html'}
# }

# static paths will be copied without parsing their contents
# STATIC_PATHS = [
#     'extra/robots.txt',
#     ]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
    },
    'output_format': 'html5',
}


PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'assets',
    'minify',
]

MINIFY = {
    'remove_all_empty_space': True,
}