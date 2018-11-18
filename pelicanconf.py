#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# THEME = "/Users/ptyagi/Developer/ptyagicodecamp/pelican-themes/aboutwilson"
THEME = "/Users/ptyagi/Developer/ptyagicodecamp/pelican-themes/mg"

AUTHOR = u'Priyanka Tyagi'
SITENAME = u'techLog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Mazatlan'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)
 #        ('Jinja2', 'http://jinja.pocoo.org/'),)
 #        ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/priyankatyagi'),
          ('About Me', 'https://about.me/priyankatyagi'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
