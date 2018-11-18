#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# THEME = "/Users/ptyagi/Developer/ptyagicodecamp/pelican-themes/aboutwilson"
THEME = "/Users/ptyagi/Developer/ptyagicodecamp/pelican-themes/voidy-bootstrap"

AUTHOR = u'Priyanka Tyagi'
SITENAME = u'techLog'
SITEURL = 'https://ptyagicodecamp.github.io/'
SITESUBTITLE ='Sub-title that goes underneath site name in jumbotron.'
SITETAG = "Text that's displayed in the title on the home page."
# Extra stylesheets, for bootstrap overrides or additional styling.
STYLESHEET_FILES = ("pygment.css", "voidybootstrap.css",)

# Put taglist at end of articles, and use the default sharing button implementation.
CUSTOM_ARTICLE_FOOTERS = ("taglist.html", "sharing.html", )
CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"

# Default sidebar template. Omit this setting for single column mode without sidebar.
SIDEBAR = "sidebar.html"

SOCIAL = (('Google+', 'http://plus.google.com/userid',
         'fa fa-google-plus-square fa-fw fa-lg'),
        ('Twitter', 'https://twitter.com/username',
         'fa fa-twitter-square fa-fw fa-lg'),
        ('LinkedIn', 'http://linkedin-url',
         'fa fa-linkedin-square fa-fw fa-lg'),
        ('BitBucket', 'http://bitbucket.org/username',
         'fa fa-bitbucket-square fa-fw fa-lg'),
        ('GitHub', 'http://github.com/username',
         'fa fa-github-square fa-fw fa-lg'),
        )


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
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),)
 #        ('Jinja2', 'http://jinja.pocoo.org/'),)
 #        ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/priyankatyagi'),
	  ('Github', 'https://github.com/ptyagicodecamp'),
	  ('Medium', 'https://medium.com/@ptyagicodecamp'),
          ('About Me', 'https://about.me/priyankatyagi'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
