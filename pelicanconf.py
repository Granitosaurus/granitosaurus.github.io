#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Base info
AUTHOR = "Bernardas Ališauskas"
SITETITLE = AUTHOR
SITEURL = "http://localhost:8000"
SITENAME = "Blog of Bernardas Ališauskas"
SITESUBTITLE = (
    "Python programmer and a goof who loves free software, video-games and heavy metal"
)
SITEDESCRIPTION = "Thoughts and Writings of Granitosaurus"
SITELOGO = SITEURL + "/images/core/granitosaurus.png"
PATH = "content"
TIMEZONE = "Europe/Paris"
DEFAULT_LANG = "en"
FAVICON = SITEURL + "/images/favicon.ico"

# Main menu
MAIN_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_RSS_ON_MENU = True
MENUITEMS = (
    ("CV", "https://stackoverflow.com/users/story/3737009?view=Timeline"),
    ("about", "/pages/about.html"),
    ("likes", "/likes"),
)
FOOTERITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)
SOCIAL = (
    ("linkedin", "https://www.linkedin.com/in/bernardas-ali%C5%A1auskas/"),
    ("github", "https://github.com/granitosaurus"),
    ("gitlab", "https://gitlab.com/granitosaurus"),
    ("pixelfed", "https://pixelfed.social/Wraptile"),
    ("mastodon", "https://mastodon.host/@wraptile"),
    ("stack-exchange", "https://stackoverflow.com/users/3737009/granitosaurus"),
    ("at", "mailto:bernardas.alisauskas@pm.me"),
    ("matrix-org", "https://matrix.to/#/@wraptile:matrix.org"),
    ("rss-square", "/atom.xml"),
    ("instagram", "https://instagram.com/wraptile_"),
)


# Feed generation is usually not desired when developing
THEME = "corvid"
AUTHOR_IMG = "images/author.jpg"
AUTHOR_WEB = "http://granitosaur.us"
TYPOGRIFY = False
# THEME based settings
CONTENT_LICENSE = "CC BY-SA 2021"  #  unused
UTTERANCES_REPO = "Granitosaurus/granitosaurus.github.io"
# TODO:
# EMAILSUB_LINK = "https://716df175.sibforms.com/serve/MUIEALpKPp8WjHrVwQOX6keZXLkJRbnFEh2y6YhTmVmT4Z0Khgbi2MFvPO1OObOrjbMi_S0M7VXkXGkcbh36H-SqEwM3dHXxdrOOXwEPGcp9rTQKkQvMkC70Dq9RmCoikia87nLsRcx0VVGmCG2zyx5s8BwpqevRmh70vKSaLe7e95yZDCROMvm2HcN3UpLw7UsFxl_UbI6TjY_e"
# OG_IMAGE = "/images/logo-og.png"
TWITTER_HANDLE = "rebsadran"
APPLAUSE_BUTTON = True
TOC_INSERT = True  # whether to insert TOC after first paragraph
TAG_DESC = {
    "async": "asynchronous programming paradigm",
    "scaling": "ensuring programs performance scales with the amount of tasks it has to perform",
    "python": "python programming language",
    "beginner": "beginner level article",
    "intermediate": "intermediate level article",
    "advanced": "advanced level article",
    "crawling": "programatically following web links to discover content",
    "discovery-methods": "ways to discover content on a website",
    "discovery": "finding content on a website",
    "indexes": "data indexing and search engines",
    "sitemap": "website content index specifically designed for web scrapers",
    "reverse-engineering": "understanding how piece of technology is working without having access to the source code",
}


# Social widget
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa",
}
COPYRIGHT_YEAR = 2019
STATIC_PATHS = ["images", "pages", "data", "extra/CNAME", "gifs"]

# CNAME fix
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}

# feed
FEED_DOMAIN = SITENAME
FEED_ATOM = "atom.xml"
FEED_RSS = "rss.xml"


# Plugins and their settings
PLUGIN_PATHS = ["../pelican-plugins"]
PLUGINS = ["shortcodes", "pelican-toc"]
SHORTCODES = {
    'image': """<a href="/images/{{src}}"><img class="bigc" src="/images/{{src}}" title="{{desc}}" loading="lazy"></img></a><figcaption>{{desc}}</figcatpion>""",
    "mp4gif": """<video width="480" height="240" autoplay loop muted title="{{desc}}"><source src="/gifs/{{src}}" type="video/mp4"></video><figcaption>{{desc}}</figcation>""",
}
TOC = {
    "TOC_HEADERS": "^h[1-6]",
    "TOC_INCLUDE_TITLE": "false",
}
