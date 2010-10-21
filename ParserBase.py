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
		self.jvm = JavaEmitter()
	
	def pushConstantInt(self, val):
		if val <= 3:
			if val == 0:
				self.jvm.emit1byte(Opcode.ICONST_0)
			elif val == 1:
				self.jvm.emit1byte(Opcode.ICONST_1)
			elif val == 2:
				self.jvm.emit1byte(Opcode.ICONST_2)
			elif val == 3:
				self.jvm.emit1byte(Opcode.ICONST_3)
		elif val <= 127:
			if val == 4:
				self.jvm.emit1byte(Opcode.ICONST_4)
			elif val == 5:
				self.jvm.emit1byte(Opcode.ICONST_5)
			else:
				self.jvm.emit2byte(Opcode.BIPUSH, val)
		elif val <= 32767:
			self.jvm.emit3byte(Opcode.SIPUSH, val)
				
	def pushConstant(self, operand):
		val = int(operand.toString())
		self.pushConstantInt(val)
		