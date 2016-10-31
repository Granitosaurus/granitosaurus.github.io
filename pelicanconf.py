#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Bernardas Ališauskas'
SITETITLE = AUTHOR
SITEURL = 'http://localhost:8000'
SITENAME = 'Blog of Bernardas Ališauskas'
SITESUBTITLE = 'Python programmer and a goof who loves free software'
SITEDESCRIPTION = 'Thoughts and Writings of Granitosaurus'
SITELOGO = SITEURL + '/images/core/me.jpg'
STACKOVERFLOW = '3737009'
FAVICON = SITEURL + '/images/favicon.ico'
MAIN_MENU = True
MENUITEMS = (
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
)
SOCIAL = (
    ('github', 'https://github.com/granitosaurus'),
    ('rss', ''),
)

PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'
# Feed generation is usually not desired when developing
THEME = 'flex-theme'
DISQUS_SITENAME = "granitosaurus"

# Social widget

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}
COPYRIGHT_YEAR = 2016
STATIC_PATHS = ['images', 'pages', 'data', 'extra/CNAME']
# CNAME fix
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
PLUGIN_PATHS = ['./pelican-plugins']
# PLUGINS = ['sitemap', 'post_stats']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}
