from ParserBase import *

class ExpressionParser(ParserBase):
	#Public
	def __init__(self, bs):
		ParserBase.__init__(self)
		#protected
		self._exprLoopStatus = None
		#private
		self._expressionToken = None
		self.source = bs
		self.et = self._expressionToken

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
		self.jvm.emit3byte(Opcode.GETSTATIC, 6);
		self.compileExpression();
		self.jvm.emit3byte(Opcode.INVOKEVIRTUAL, 7);
		self.jvm.emit1byte(Opcode.RETURN);
		self.jvm.finish();
		
	def _expression(self):
		tt = self._expressionToken.getTokenType()
		if tt == TokenType.SYMBOL or tt == TokenType.LITERAL or tt == TokenType.L_PAREN:
			self._term()
			self._expression2()
		else:
			self.setError("Syntax error in expression at " + self._expressionToken.toString() + self.source.fln())
	
	def _expression2(self):
		tkn = None
		if isinstance(self._expressionToken, Token):
			tkn = self._expressionToken.toString()
		
		if tkn == "+":
			self._match(TokenType.ADD_OP)
			self._term()
			self.jvm.emit1byte(Opcode.IADD)
			self._expression2()
		elif tkn == "-":
			self._match(TokenType.ADD_OP)
			self._term()
			self.jvm.emit1byte(Opcode.ISUB)
			self._expression2()
		else:
			pass
		
	def _factor(self):
		tt = self._expressionToken.getTokenType()
		
		if tt == TokenType.SYMBOL:
			sym = self._symbols.get(self._expressionToken.toString())
			if sym.getSymbolType() == SymbolType.ARRAY:
				self.jvm.chooseOp(Opcode.ALOAD, Opcode.ALOAD_0, sym.getAddress())
				nt = self.source.peekToken()
				print "AFTER ALOAD NEXT TOKEN ---- ", nt.toString()
				if nt.toString() == ".":
					print "DOT MOTHER FUCKER"
					nt = self.source.nextToken()
					nt = self.source.peekToken()
					print nt.toString(), "<<"
					if nt.toString() == "length":
						print "GET ME THAT LENGTH"
						self._getExpressionToken()
						print nt.toString(), nt.getTokenType(), self._expressionToken.toString(), "penis"
						self.jvm.emit1byte(Opcode.ARRAYLENGTH)
						self._match(TokenType.SYMBOL)

						
				elif nt.toString() == "[":
					self._getExpressionToken()
					self.compileExpression()
					e = self._expressionToken.toString()
					print e, "EXPRESSION TOKEN"
					self.jvm.emit1byte(Opcode.IALOAD)
					self._match(TokenType.R_BRACKET)
					
			elif sym.getSymbolType() == SymbolType.VARIABLE:
				self.jvm.chooseOp(Opcode.ILOAD, Opcode.ILOAD_0, sym.getAddress())
				self._match(TokenType.SYMBOL)

		elif tt == TokenType.LITERAL:
			self.showMessage("pushed constant: " + self._expressionToken.toString()) #push constant
			self.pushConstant(self._expressionToken)
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
			self.showMessage("Expression token: " + self._expressionToken.toString() + "\n")
	
	def _match(self, tt):
		if (self._expressionToken.getTokenType() == tt):
			self._getExpressionToken()
		else:
			self.setError("Syntax error at " + self._expressionToken.toString() + self.source.fln())
			
	def _term(self):
		tt = self._expressionToken.getTokenType()
		if tt == TokenType.SYMBOL or tt == TokenType.LITERAL or tt == TokenType.L_PAREN:
			self._factor()
			self._term2()
		else:
			self.setError("Syntax error in term at " + self._expressionToken.toString() + self.source.fln())
		
	def _term2(self):
		tkn = self._expressionToken.toString()
		
		if tkn == "*":
			self._match(TokenType.MULT_OP)
			self._factor()
			self.jvm.emit1byte(Opcode.IMUL)
			self._term2()
		elif tkn == "/":
			self._match(TokenType.MULT_OP)
			self._factor()
			self.jvm.emit1byte(Opcode.IDIV)
			self._term2()
		else:
			pass