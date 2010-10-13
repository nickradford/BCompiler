class ExpressionParser(ParserBase):
	#Public
	def __init__(self):
		super.__init__(self)
	def compileExpression(self):
		pass
	def testExpression(self, fileName):
		pass
		
	#protected
	_exprLoopStatus = None
	#private
	_expressionToken = None
	def _expression(self):
		pass
	def _expression2(self):
		pass
	def _factor(self):
		pass
	def _getExpressionToken(self):
		pass
	def _match(self, tt):
		pass
	def _term(self):
		pass
	def _term2(self):
		pass
	def _mname(self, arg):
		pass