# -*- coding: utf-8 -*- #

from datetime import datetime

AUTHOR = 'Priyanka Tyagi'
SITENAME = 'techLog'
SITETITLE = 'techLog'
SITEURL = 'https://ptyagicodecamp.github.io'
SITESUBTITLE ='Explore | Android | Flutter | Software Engineering'
SITEDESCRIPTION = "Mobile engineering tech logger."

SITELOGO = 'https://ptyagicodecamp.github.io/images/profile.jpg'
FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

THEME = '/Users/ptyagi/Developer/ptyagicodecamp/pelican-themes/Flex'
PATH = 'content/'
OUTPUT_PATH = 'blog/'
TIMEZONE = 'America/New_York'

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml' #'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

LINKS = (
        ('Support', 'https://www.paypal.me/pritya'),
        # ('LinkedIn', 'https://www.linkedin.com/in/priyankatyagi'),
        # ('GitHub', 'https://github.com/ptyagicodecamp'),
        # ('Medium', 'https://medium.com/@ptyagicodecamp'),
        # ('Twitter', 'https://twitter.com/ptyagi13'),
        # ('YouTube', 'https://www.youtube.com/channel/UCO3_dbHasEnA2dr_U0EhMAA?view_as=subscriber')
	)

SOCIAL = (
        ('linkedin', 'https://www.linkedin.com/in/priyankatyagi'),
        ('github', 'https://github.com/ptyagicodecamp'),
        ('medium', 'https://medium.com/@ptyagicodecamp'),
        ('twitter', 'https://twitter.com/ptyagi13'),
        ('youtube', 'https://www.youtube.com/channel/UCO3_dbHasEnA2dr_U0EhMAA?view_as=subscriber'),
        ('codementor', 'https://www.codementor.io/ptyagicodecamp')
        #('rss', '/blog/feeds/all.atom.xml'),
	)

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10

DISQUS_SITENAME = "https-ptyagicodecamp-github-io"
ADD_THIS_ID = 'ra-5cf387135c8761da'

STATIC_PATHS = ['images', 'media']

CUSTOM_CSS = 'static/custom.css'

USE_LESS = True

GITHUB_CORNER_URL = 'https://github.com/ptyagicodecamp'

GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-6359982310050489',
    'page_level_ads': True,
    'ads': {
        'aside': '8977779775',
        #'main_menu': '8977779775',
        #'index_top': '8977779775',
        'index_bottom': '8977779775',
        'article_top': '6546879945',
        'article_bottom': '6546879945',
    }
}
