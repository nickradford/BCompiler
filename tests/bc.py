import sys
sys.path.append("../")

from BScanner import *
from BParser import *


bp = BParser()
bp.compile("test.txt")