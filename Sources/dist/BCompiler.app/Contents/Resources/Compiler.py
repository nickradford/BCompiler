#------------------------ Compiler.py ------------------------#
#
# Implemented from code provided by Dr. Lancaster
#
#
# This class handles errors, warnings, and informational messages
# that are written to standard output.  Methods are provided to handle
# debugFlag.  The first time debugFlag becomes true, the debug output
# file is opened.
#
# All data and methods are static.  This class is the base class for
# BScanner, ParserBase, and JavaEmitter.  Certain methods are global
# and can be access from throughout the compiler.
#
#-----------------------------------------------------------#

from SymbolTable import *
from CompilerException import *

class Compiler:
	_debugFlag = False
	_debugFile = None
	_symbols = SymbolTable()
    
	@staticmethod
	def char2string(ch):
		return str(ch)
		
	@staticmethod
	def long2string(val):
		return str(val)
		
	@staticmethod    
	def debugOff():
		Compiler._debugFlag = False
		
	@staticmethod
	def debugOn():
		Compiler._debugFlag = True
		if Compiler._debugFile is None:
			Compiler._debugFile = open("../debug.txt", 'w')
			if Compiler._debugFile is None:
				Compiler.setError("Couldn't open debug file 'run.txt'")

	@staticmethod	
	def debugging():
		return Compiler._debugFlag
    
	@staticmethod
	def setError(error):
		print error
		raise CompilerException(error)
	
	@staticmethod
	def setWarning(warning):
		Compiler.showMessage("Warning: " + warning)
		
	@staticmethod
	def showMessage(message, message2 = None, message3 = None):
		if Compiler._debugFlag is True:
			Compiler._debugFile.write(message + "\n")