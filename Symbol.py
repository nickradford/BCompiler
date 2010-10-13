#------------------------ Symbol.py ------------------------#
#
# Implemented from code provided by Dr. Lancaster
#
#
# The Symbol class represents a symbol defined in a B program.  This
# file also defines enum types used to indicate the scope and type of
# each symbol.
#
#-----------------------------------------------------------#

from Token import *
  
class SymbolScope: #enum SymbolScope
    GLOBAL, LOCAL = range(2)
    
class SymbolType: #enum SymbolType
    VARIABLE, ARRAY, DEFINED_FUNCTION, FORWARD_FUNCTION = range(4)
    

class Symbol(Token):
	def __init__(self, name, ptype, scope):
		Token.__init__(self, TokenType.SYMBOL, name)
		self._scope = scope
		self._symbolType = ptype
		self._address = -1
		
	def getScope(self):
		return self._scope
		
	def getSymbolType(self):
		return self._symbolType
		
	def getAddress(self):
		return self._address
		
	def setAddress(self, address):
		self._address = address
    
	def setSymbolType(self, symType):
		self._symbolType = symType
    