#bexp.py

import sys
from ExpressionParser import *

if len(sys.argv) == 1 or len(sys.argv) > 3 or not ".txt" in sys.argv[1]:
	#print "\nUsage: bexp <filename>\n"

fileName = sys.argv[len(sys.argv) - 1]
if sys.argv[1] == "-d":
	Compiler.debugOn()

exp = ExpressionParser()
exp.testExpression(fileName)
#print "done"