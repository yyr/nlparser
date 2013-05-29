"""
Read and manipulate the Fortran namelist files. Regexp based parsing.

Fotran namelist files are in the following pattern.

     &section1
        par = val
        par2 = val,val2
        ...
     /

     &section2
        par = val
        par4 = val,val2
        ...
     /
"""

import re

VARSTRING = r'\b[a-zA-Z][a-zA-Z0-9_]*\b'
SPACES = r'[\t\s]*'
RE_EMPTY_LINE = re.compile(r'[\t\s]*\n')
RE_SECT_NAME = re.compile(r"[\t\s]*&(" + VARSTRING + r")[\t\s]*$")
RE_SECT_END = re.compile(r"^[\t\s]*[/|\$END|\$end][\t\s]*")
RE_COMMENT_LINE = re.compile(r'^[\t\s]*!')


class Namelist(object):
    """Read and Keep the Fortran namelist files. """
    def __init__(self, lines, filename="<lines>"):
        self._filename = filename
        self._raw = lines

    @property
    def raw(self):
        return self._raw

    def lines_to_sections(self, lines=None):
        """ split into sections, remove empty line and comment line"""
        if not lines:
            lines = self.raw

        section = []
        sections = []
        for l in lines:
            if RE_EMPTY_LINE.search(l) or RE_COMMENT_LINE.search(l) or l == '':
                continue        # clean comment line and empty lines.

            if RE_SECT_NAME.search(l):
                section = []

            section.append(l)

            if RE_SECT_END.search(l):
                # sections[sec_name] = section
                sections.append(section)
                section = []

        return sections
