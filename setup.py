from distutils.core import setup

import nlparser

setup(
    name = 'nlparser',
    version = nlparser.__version__,
    author = nlparser.__license__,
    author_email = 'hi@yagnesh.org',
    url = nlparser.__website__,
    license = nlparser.__license__,
    description = 'nlparser - Python module to manipulate Fortran namelist files.'
    long_description = nlparser.__doc__,
    keywords = 'Fortran, f90, namelist, parser'
)
