# -*- coding: utf-8 -*-
#
# ACCwebsite documentation build configuration file, created by
# sphinx-quickstart on Sun Mar 22 20:09:55 2015.
#
import sys
import os
import shlex
import sphinx_rtd_theme

# -- General configuration ------------------------------------------------
extensions = [
        'tut.sphinx',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'ACCwebsite'
copyright = u'2015, Roie R. Black'
author = u'Roie R. Black'
version = '0.4'
release = '0.4'
language = None
today_fmt = '%B %d, %Y'
exclude_patterns = ['_build', '_venv', 'code']
pygments_style = 'sphinx'
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------
html_theme = 'sphinx_rtd_theme'
#html_theme_options = {}
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
#html_favicon = None
html_static_path = ['_static']
html_last_updated_fmt = '%b %d, %Y'
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'letterpaper',
'pointsize': '12pt',
#'preamble': '',
#'figure_align': 'htbp',
}

latex_documents = [
  (master_doc, 'ACCwebsite.tex', u'ACCwebsite Documentation',
   u'Roie R. Black', 'manual'),
]
