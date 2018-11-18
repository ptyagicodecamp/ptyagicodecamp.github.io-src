#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://ptyagicodecamp.github.io'
RELATIVE_URLS = True

#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = False

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'


# Following items are often useful when publishing

DISQUS_SITENAME = "https://disqus.com/by/ptyagicodecamp/"
GOOGLE_ANALYTICS = "UA-54296314-10"
GOOGLE_ANALYTICS_SITEID = "techlog"
TWITTER_USERNAME = "ptyagi13"
