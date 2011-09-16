project = u'flatland'
copyright = u'2008-2011, the flatland authors and contributors'

version = '0.0'
release = '0.0.hg-tip'


master_doc = 'index'
add_module_names = False
default_role = 'py:obj'


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.spelling',
]


autodoc_default_flags = ['members', 'show-inheritance']


intersphinx_mapping = {
    'http://docs.python.org/': None,
    'http://discorporate.us/projects/Blinker/docs/tip/': None,
}


spelling_ignore_pypi_package_names = True


html_theme_path = ['_themes']
html_theme = 'flatland'
html_show_sourcelink = False
html_sidebars = {
    'index': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'],
}
