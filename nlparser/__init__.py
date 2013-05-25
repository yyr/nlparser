# Import README.rst using cog
# [[[cog
# from cog import out
# out('"""\n{0}\n"""'.format(file('../README.rst').read()))
# ]]]
"""
==========================================================================
    nlparser - Python module to manipulate Fortran namelist files.
==========================================================================

# [[[end]]]
DATE    = "Thursday, May 25 2013"
AUTHOR  = "Yagnesh Raghava Yakkala"
WEBSITE = "http://github.com/yyr/nlparser"
LICENSE = "GPL v3 or later"
VERSION = '0.1-dev'

from .core import NameList


def parse_lines(lines, filename):
    """
    """
    return Namelist(lines, filename=filename)






if __name__ == '__main__':
    main()
