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

class Compiler:
	def __init__(self, arg):
		_debugFlag = False
		_debugFile = None
		_symbols = SymbolTable()
    
    
	def char2string(self, ch):
		pass
		
	@staticmethod
	def long2string(self, val):
		return str(val)
    
	def debugOff(self):
		self._debugFlag = False
	
	def debugOn(self):
		self._debugFlag = True
		if self._debugFile is None:
			self._debugFile = open("run.txt")
			if self._debugFile is None:
				self.setError("Couldn't open debug file 'run.txt'")
	
	def debugging(self):
		return self._debugFlag
    
	@staticmethod
	def setError(self, error):
		print error
	def setWarning(self, warning):
		pass
	def showMessage(self, message, message2 = None, message3 = None):
		if self._debugFlag is True:
			self._debugFile.write(message)
    # def showMessage(self, message1, message2, message3):
    #         if self._debugFlag is True:
    #             self._debugFile.write("{:<}Current Op: {:10}")
    
	def _buildMessage(self, type, string):
		pass