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
		self._locals.deleteAll();                 	
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
		pass                       	
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
			i = 0
			for item in self._globals:
				C.Compiler.showMessage(str(i) + "\t " + item + "\n")
		else:	
			i = 0
			for item in self._locals:
				C.Compiler.showMessage(str(i) + "\t " + item + "\n")

from Compiler import *                     	