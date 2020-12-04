# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]
if os.getenv("SPELLCHECK"):
    extensions += ("sphinxcontrib.spelling",)
    spelling_show_suggestions = True
    spelling_lang = "en_US"

source_suffix = ".rst"
master_doc = "index"
project = "vardef"
year = "2020"
author = "Rodrigo Martins de Oliveira"
copyright = "{0}, {1}".format(year, author)
version = release = "0.1.0"

pygments_style = "trac"
templates_path = ["."]
extlinks = {
    "issue": ("https://github.com/allrod5/vardef/issues/%s", "#"),
    "pr": ("https://github.com/allrod5/vardef/pull/%s", "PR #"),
}
import sphinx_py3doc_enhanced_theme

html_theme = "sphinx_py3doc_enhanced_theme"
html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]
html_theme_options = {
    "githuburl": "https://github.com/allrod5/vardef/",
    "body_max_width": "90%",
}

html_use_smartypants = True
html_last_updated_fmt = "%b %d, %Y"
html_split_index = False
html_sidebars = {"**": ["searchbox.html", "globaltoc.html", "sourcelink.html"]}
html_short_title = "%s-%s" % (project, version)

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
