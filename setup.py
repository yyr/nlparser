from distutils.core import setup

import nlparser

setup(
    name = 'nlparser',
    version = nlparser.VERSION,
    author = nlparser.LICENSE,
    author_email = 'hi@yagnesh.org',
    packages = ['nlparser'],
    url = nlparser.WEBSITE,
    license = nlparser.LICENSE,
    description = 'nlparser - Python module to parse f90 Fortran namelist files.',
    long_description = nlparser.__doc__,
    keywords = 'Fortran, f90, namelist, parser',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
    ],

)
