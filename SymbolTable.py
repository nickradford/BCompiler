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
		pass                       	
	def get(self, name):           	
		pass                       	
	def insert(self, sym):         	
		name = sym.toString()                     	
		                           	
	#Private:                      	
	             	
	def _dumpOneTable(self, table):	
		pass                       	