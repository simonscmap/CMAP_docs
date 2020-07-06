# -*- coding: utf-8 -*-
import sys
import os
import datetime
import sphinx_rtd_theme
# import sphinx_gallery
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import sys
import os

sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------

project = 'Simons CMAP'
copyright = ''
author = ''

# The short X.Y version
version = '0.0.1'
# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
    'sphinx.ext.extlinks',
    "sphinx.ext.intersphinx",
    "nbsphinx",
    "recommonmark",
    'sphinx_markdown_tables'
]



source_suffix = ['.rst', '.md']

nbsphinx_allow_errors = True
nbsphinx_timeout = 1200
html_scaled_image_link = False
# Always show the source code that generates a plot
plot_include_source = True
plot_formats = ['png']

# Add any paths that contain templates here, relative to this directory.

# Sphinx project configuration
templates_path = ['_templates']
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# The encoding of source files.
source_encoding = 'utf-8-sig'
master_doc = 'index'


# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store','catalog/dataset_descriptions/*.md']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.



html_last_updated_fmt = '%b %d, %Y'
html_title = 'CMAP'
html_short_title = 'CMAP'
html_logo = '_static/CMAP_logos/CMAP_logo.png'
html_favicon = '_static/CMAP_logos/CMAP_logo.png'
html_static_path = ['_static']
html_extra_path = []
pygments_style = 'default'
add_function_parentheses = False
html_show_sourcelink = False
html_show_sphinx = True
html_show_copyright = True


# Theme config
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    'logo_only': False,
    'display_version': False,
    'prev_next_buttons_location': None,
    'navigation_depth': 4,
    'collapse_navigation': True
}

html_context = {
    'menu_links_name': 'Outside Resources',
    'menu_links': [
        ('<i class="fa fa-globe fa-fw"></i> Simons CMAP Web Application', 'https://simonscmap.com/'),
        ('<i class="fa fa-archive fa-fw"></i> Interactive Data Catalog', 'https://simonscmap.com/catalog'),
        ('<i class="fa fa-github fa-fw"></i> Project Source Code', 'https://github.com/simonscmap'),
        ('<i class="fa fa-slack fa-fw"></i> Slack', 'https://join.slack.com/t/simons-cmap/shared_invite/enQtNjQzMTkzMjg0NjQ2LTdlOGRhZjNhMDY3MjRlNjg2OTY5NzE3ZWZhNWE0OWZhYmQzMTJjNDkyNDQ1MjNkZDg0N2MzMzhlZDliNGYxYzQ'),
    ]
}



# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Load the custom CSS files (needs sphinx >= 1.6 for this to work)
def setup(app):
    app.add_stylesheet("style.css")
#
