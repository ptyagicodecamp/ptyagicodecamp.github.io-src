#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# THEME = "/Users/ptyagi/Developer/ptyagicodecamp/pelican-themes/aboutwilson"
THEME = "/Users/ptyagi/Developer/ptyagicodecamp/pelican-themes/voidy-bootstrap"

AUTHOR = u'Priyanka Tyagi'
SITENAME = u'techLog'
SITEURL = 'https://ptyagicodecamp.github.io'
SITESUBTITLE ='Explore | Android | Software Engineering'
SITETAG = "Android tech logger."
# Extra stylesheets, for bootstrap overrides or additional styling.
STYLESHEET_FILES = ("pygment.css", "voidybootstrap.css",)

# Put taglist at end of articles, and use the default sharing button implementation.
CUSTOM_ARTICLE_FOOTERS = ("taglist.html", "sharing.html", )
CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"

# Default sidebar template. Omit this setting for single column mode without sidebar.
SIDEBAR = "sidebar.html"
CUSTOM_FOOTER = "custom/footer.html"

SOCIAL = (
        ('LinkedIn', 'https://www.linkedin.com/in/priyankatyagi',
         'fa fa-linkedin-square fa-fw fa-lg'),
        ('GitHub', 'https://github.com/ptyagicodecamp',
         'fa fa-github-square fa-fw fa-lg'),
        ('Medium', 'https://medium.com/@ptyagicodecamp',
         'fa fa-bitbucket-square fa-fw fa-lg'),
	('Google+', 'https://plus.google.com/u/0/114534305132859234440',
         'fa fa-google-plus-square fa-fw fa-lg'),
        ('Twitter', 'https://twitter.com/ptyagi13',
         'fa fa-twitter-square fa-fw fa-lg'),
	)



PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
