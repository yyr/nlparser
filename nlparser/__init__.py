# Import README.rst using cog
# [[[cog
# from cog import out
# out('"""\n{0}\n"""'.format(file('../README.rst').read()))
# ]]]
"""
==========================================================================
    nlparser - Python module to manipulate Fortran namelist files.
==========================================================================

"""
# [[[end]]]

DATE    = "Thursday, May 25 2013"
AUTHOR  = "Yagnesh Raghava Yakkala"
WEBSITE = "http://github.com/yyr/nlparser"
LICENSE = "GPL v3 or later"
VERSION = '0.1-dev'

import codecs
from .core import Namelist


def _parse_lines(lines, filename):
    return Namelist(lines, filename=filename)


def load(filename):
    nlfile = codecs.open(filename, encoding='utf8')
    return loadi([ l.rstrip('\n') for l in nlfile.readlines()],
                 "<file>")


def loads(string):
    return loadi(string.splitlines(), "<lines>")


def loadi(lines,filename):
    print(lines)
    return _parse_lines(lines, filename)

if __name__ == '__main__':
    pass
