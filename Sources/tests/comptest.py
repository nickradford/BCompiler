import sys
sys.path.append("../")

from Compiler import *

c = Compiler()

c.debugOn()

c.showMessage("message")
print "message shown"