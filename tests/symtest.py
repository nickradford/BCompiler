import sys
sys.path.append("../")

import Compiler
from SymbolTable import *
from Symbol import *
s = SymbolTable()

i=0
while i< 100:
	sym = Symbol("var" + str(i), SymbolType.VARIABLE, i%2)
	s.insert(sym)
	i += 1
	
Compiler.Compiler.debugOn()


s.dump()