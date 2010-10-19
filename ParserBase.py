#----------------------- ParserBase.py -----------------------#
#
# Implemented from code provided by Dr. Lancaster
#
#
# ParserBase is the base class for BParser and ExpressionParser.
# It contains data and methods used by both.
#
#----------------------------------------------------------#
from BScanner    import *
from Compiler    import *
from JavaEmitter import *

class Status():
	CONTINUE, FREEZE, EXIT = range(3);
		

class ParserBase(Compiler):
	def __init__(self):
		self.source = None
	
	def pushConstant(self, val):
		pass	
		
	def pushConstant(self):
		pass