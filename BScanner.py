from Compiler import *
from MyMap import *
from Token import *


class BScanner(Compiler):
	def __init__(self, fileName):
		Compiler.__init__(self)
		self._lineNumber = None
		self._operators = None
		self._saveToken = None
		try:
			self._sourceFile = open(fileName)
		except:
			setError("error")
			
	def getLineNumber(self):
		return self._lineNumber
	def nextToken(self):
		pass
	def peekToken(self):
		pass
    
    #private
	def _isOctalDigit(self, c):
		if char >= '0' and char <= '7':
			return True
	def _readCharacter(self):
		pass
	def _readLiteral(self, firstChar):
		pass
	def _readSymbol(self, firstChar):
		pass
	def _unreadCharacter(self, c):
		pass