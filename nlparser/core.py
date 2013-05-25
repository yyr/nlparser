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


class Namelist(dict):
    """Read and Keep the Fortran namelist files. """
    def __init__(self, lines, filename="<undefined>"):
        self.__init__(self)
        self._filename = filename
        self._lines = lines
        self.update(self.parse())

    def parse(self):
        # re patterns
        varstring = r'\b[a-zA-Z][a-zA-Z0-9_]*\b'
        spaces = r'[\t\s]*'

        sectname = re.compile(r"^[\t\s]*&(" + varstring + r")[\t\s]*$")
        sectend = re.compile(r"^[\t\s]*/[\t\s]*$")

        nl = {}                 # this is going to returned
        sect = ''

        for line in self._lines.split("\n+"):
            if re.match(secname, line):
                sect = re.sub(secname, r"\1",line)
                nl[sect] = {
                    'raw' : [],
                    'par' : [{}]
                }
            elif re.match(re.sub):
                pass
