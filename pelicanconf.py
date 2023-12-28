AUTHOR = 'Kayla Gulka'
SITENAME = 'Kayla Gulka'
SITEURL = "https://gulk.dev"

PATH = "content"

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'English'

# Kayla stuff :))))
USE_FOLDER_AS_CATEGORY = True
DELETE_OUTPUT_DIRECTORY = True
THEME = "theme"
STATIC_PATHS = ['static']
EXTRA_PATH_METADATA = {'static/CNAME' : {'path': 'CNAME'},}

CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
TAG_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True