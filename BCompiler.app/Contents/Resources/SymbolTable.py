#------------------------ SymbolTable.py ------------------------#
#
# Implemented from code provided by Dr. Lancaster
#
#
# This class is used to maintain information about every user-defined
# symbol in the source program.  There is a global symbol table for names
# known throughout the program, and a local symbol table for names known
# only within the current function.  An exception is thrown if an attempt
# is made to add an existing name to a symbol table or if a request is made
# for an undeclared symbol.
#
#----------------------------------------------------------------#


from MyMap import *
from Symbol import *
import Compiler as C

class SymbolTable:
	def __init__(self):
		self._globals = MyMap()             	
		self._locals = MyMap()
		
	def clearLocalTable(self):
		self._locals.deleteAll()
		               	
	def defined(self, name):
		if self._locals.defined(name):
			return True;
		elif self._globals.defined(name):
			return True
		else:
			return False
			
	def dump(self):                	
		if len(self._locals) + len(self._globals) == 0:
			C.Compiler.showMessage("\n***Symbol tables are empty***\n")
		else:
			C.Compiler.showMessage("")
			C.Compiler.showMessage("***Global Symbol Table***\n")
			self._dumpOneTable("global")
			C.Compiler.showMessage("***Local Symbol Table***\n")
			self._dumpOneTable(self._locals)
			C.Compiler.showMessage("***End of symbol table dump***\n")
			C.Compiler.showMessage("")
		return
					         	
	def get(self, name):           	
		if self._locals.defined(name):
			return self._locals[name]
		elif self._globals.defined(name):
			return self._globals[name]
		else:	
			C.Compiler.setError("Symbol not declared: " + name)
			raise CompilerException("Symbol not declared: " + name)
			
				
	def insert(self, sym):         	
		name = sym.toString()  
		if sym.getScope() == SymbolScope.GLOBAL and self._globals.defined(name):
			C.Compiler.setError("Duplicate declaration for " + name)
		if sym.getScope() == SymbolScope.LOCAL and self._locals.defined(name):
			C.Compiler.setError("Duplicate declaration for " + name)
		
		if sym.getScope() == SymbolScope.GLOBAL:
			self._globals[name] = sym
		else:
			self._locals[name] = sym
		                           	
	#Private:                      	
	             	
	def _dumpOneTable(self, table):
		if table == "global":
			for item in self._globals:
				symbol = self._globals[item]
				addr = C.Compiler.long2string(symbol.getAddress())
				level = "G"
				if symbol.getSymbolType() == SymbolType.VARIABLE:
					symbolType = "VARIABLE"
				elif symbol.getSymbolType() == SymbolType.ARRAY:
					symbolType = "ARRAY"
				elif symbol.getSymbolType() == SymbolType.DEFINED_FUNCTION:
					symbolType = "DEFINED_FUNCTION"
				else:
					symbolType = "FORWARD_FUNCTION"
				
				line = symbol.toString() + ", " + addr + ", " + level + ", " + symbolType +"\n"
				C.Compiler.showMessage(line)
		else:	
			for item in self._locals:
				symbol = self._locals[item]
				addr = C.Compiler.long2string(symbol.getAddress())
				level = "L"
				if symbol.getSymbolType() == SymbolType.VARIABLE:
					symbolType = "VARIABLE"
				elif symbol.getSymbolType() == SymbolType.ARRAY:
					symbolType = "ARRAY"
				elif symbol.getSymbolType() == SymbolType.DEFINED_FUNCTION:
					symbolType = "DEFINED_FUNCTION"
				else:
					symbolType = "FORWARD_FUNCTION"
				
				line = symbol.toString() + ", " + addr + ", " + level + ", " + symbolType +"\n"
				C.Compiler.showMessage(line)

from Compiler import *                     	