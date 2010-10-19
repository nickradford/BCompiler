from ParserBase import *

class ExpressionParser(ParserBase):
	#Public
	def __init__(self):
		ParserBase.__init__(self)
		#protected
		self._exprLoopStatus = None
		#private
		self._expressionToken = None

	def compileExpression(self):
		#   This function initiates the compilation of an arithmetic
	    #   expression.  This algorithm is top-down even though the rest
	    #   of the compiler is bottom-up.
	    self._getExpressionToken();
	    self._expression();
	    self.showMessage(" ");
	    return self._expressionToken;
	
	def testExpression(self, fileName):
		self.source = BScanner(fileName)
		
		# Debug is on by default when testing
		self.debugOn();
	
		# Generate code to print the value of an expression
		# read from the source file
		#* jvm.emit(GETSTATIC, 6);
		self.compileExpression();
		#* jvm.emit(INVOKEVIRTUAL, 7);
		#* jvm.emit(RETURN);
		#* jvm.finish();
		
	def _expression(self):
		tt = self._expressionToken.getTokenType()
		if tt == TokenType.SYMBOL:
			pass
		elif tt == TokenType.LITERAL:
			self._term()
			self._expression2()
		elif tt == TokenType.L_PAREN:
			self._term()
			self._expression2()
		else:
			self.setError("Syntax error in expression at " + self._expressionToken.toString())
	
	def _expression2(self):
		tkn = None
		if isinstance(self._expressionToken, Token):
			tkn = self._expressionToken.toString()
		
		if tkn == "+":
			self._match(TokenType.ADD_OP)
			self._term()
			self.showMessage("+")
			self._expression2()
		elif tkn == "-":
			self._match(TokenType.ADD_OP)
			self._term()
			self.showMessage("-")
			self._expression2()
		else:
			pass
		
	def _factor(self):
		tt = self._expressionToken.getTokenType()
		
		if tt == TokenType.SYMBOL:
			self.setError("Symbols not allowed")
		elif tt == TokenType.LITERAL:
			self.showMessage(self._expressionToken.toString())
			self._match(TokenType.LITERAL)
		elif tt == TokenType.L_PAREN:
			self._match(TokenType.L_PAREN)
			self._expression()
			self._match(TokenType.R_PAREN)
		else:
			pass	
		
	def _getExpressionToken(self):
		self._expressionToken = self.source.nextToken()
		print "Debug: " + str(self._expressionToken)
		if isinstance(self._expressionToken, Token):
			print "\t" + self._expressionToken.toString()
			self.showMessage("Expression token: " + self._expressionToken.toString())
	
	def _match(self, tt):
		if (self._expressionToken.getTokenType() == tt):
			self._getExpressionToken()
		else:
			self.setError("Syntax error at " + self._expressionToken.toString())
			
	def _term(self):
		tt = self._expressionToken.getTokenType()
		if tt == TokenType.SYMBOL:
			pass
		elif tt == TokenType.LITERAL:
			self._factor()
		elif tt == TokenType.L_PAREN:
			pass
		else:
			self.setError("Syntax error in term at " + self._expressionToken.toString())
		
	def _term2(self):
		tkn = self._expressionToken.toString()
		
		if tkn == "*":
			self._match(TokenType.MULT_OP)
			self._factor()
			self.showMessage("*")
			self._term2()
		elif tkn == "/":
			self._match(TokenType.MULT_OP)
			self._factor()
			self.showMessage("/")
			self._term2()
		else:
			pass