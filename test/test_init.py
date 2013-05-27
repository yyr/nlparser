from os.path import dirname, abspath
import sys

TESTDIR = dirname(abspath(__file__))
ROOTDIR = dirname(test_dir)
sys.path.append(ROOTDIR)

DATADIR = os.path.join(dirname(__file__),'data')

nlparser.loads("""
&section1
par = val
par2 = val,val2
/
""")
