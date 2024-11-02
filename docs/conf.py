import os
import sys

sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------
project = 'pycicd'
author = 'Weston Partin'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',      # Automatically document from docstrings
    'sphinx.ext.autosummary',  # Enables automatic summation features
    'sphinx.ext.doctest',      # Enables documentation testing
    'sphinx.ext.napoleon',     # Support for Google and NumPy style docstrings
    'sphinx.ext.viewcode',     # Add links to highlighted source code
    'sphinx.ext.todo',         # Support for todo items
]
autosummary_generate = True

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'  # Change to 'sphinx_rtd_theme' if you prefer that
html_static_path = []