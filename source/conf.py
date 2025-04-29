# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'digital-phenotyping-server (TTRU-SMG)'
copyright = '2025, Sourabh Swargam'
author = 'Sourabh Swargam'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # to import project modules if needed

# Theme
html_theme = 'sphinx_rtd_theme'

# Output directory
html_static_path = ['_static']