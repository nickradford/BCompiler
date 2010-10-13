import sys
sys.path.append("../")

import Compiler
from SymbolTable import *
from Symbol import *

sym = Symbol("var", SymbolType.VARIABLE, SymbolScope.LOCAL)
s = SymbolTable()
Compiler.Compiler.debugOn()
s.insert(sym)

s.dump()