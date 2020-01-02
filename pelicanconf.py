#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Base info
AUTHOR = 'Bernardas Ališauskas'
SITETITLE = AUTHOR
SITEURL = 'http://localhost:8000'
SITENAME = 'Blog of Bernardas Ališauskas'
SITESUBTITLE = 'Python programmer and a goof who loves free software, video-games and heavy metal'
SITEDESCRIPTION = 'Thoughts and Writings of Granitosaurus'
SITELOGO = SITEURL + '/images/core/granitosaurus.png'
PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
FAVICON = SITEURL + '/images/favicon.ico'

# Main menu
MAIN_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_RSS_ON_MENU = True
MENUITEMS = (
    ('about', '/pages/about.html'),
)
FOOTERITEMS = (
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
)
SOCIAL = (
    ('github', 'https://github.com/granitosaurus'),
    ('gitlab', 'https://gitlab.com/granitosaurus'),
    ('pixelfed', 'https://pixelfed.social/Wraptile'),
    ('mastodon', 'https://mastodon.host/@wraptile'),
    ('stack-exchange', 'https://stackoverflow.com/users/3737009/granitosaurus'),
    ('at', 'mailto:bernardas.alisauskas@pm.me'),
    ('matrix-org', 'https://matrix.to/#/@wraptile:matrix.org'),
    ('rss-square', '/atom.xml'),
)


# Feed generation is usually not desired when developing
THEME = 'medius'

# Social widget
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}
COPYRIGHT_YEAR = 2019
STATIC_PATHS = ['images', 'pages', 'data', 'extra/CNAME', 'gifs']

# CNAME fix
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

# feed
FEED_DOMAIN = SITENAME
FEED_ATOM = 'atom.xml'
FEED_RSS = 'rss.xml'


# Plugins and their settings
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['shortcodes', 'pelican-toc']
SHORTCODES = {
    'image': """<a href="/images/{{src}}"><img src="/images/{{src}}" title="{{desc}}"></img></a><figcaption>{{desc}}</figcatpion>""",
    'mp4gif': """<video width="480" height="240" autoplay loop muted title="{{desc}}"><source src="/gifs/{{src}}" type="video/mp4"></video><figcaption>{{desc}}</figcation>"""

}
TOC = {
    'TOC_HEADERS': '^h[1-6]',
    'TOC_INCLUDE_TITLE': 'false',
}

