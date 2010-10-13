#----------------------- ParserBase.py -----------------------#
#
# Implemented from code provided by Dr. Lancaster
#
#
# ParserBase is the base class for BParser and ExpressionParser.
# It contains data and methods used by both.
#
#----------------------------------------------------------#
import BScanner
import Compiler
import JavaEmitter

class Status():
	CONTINUE, FREEZE, EXIT = range(3);
		

class ParserBase(Compiler):
	def __init__(self, arg):
		super(ParserBase, self).__init__()
		self.arg = arg
	
	def pushConstant(self, val):
		pass	
		
	def pushConstant()