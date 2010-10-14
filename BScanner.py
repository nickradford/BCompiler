from Compiler import *
from MyMap import *
from Token import *
from EOFException import *
import re

class BScanner(Compiler):
	def __init__(self, fileName):
		self._lineNumber = 0
		self._operators = {}
		self._saveToken = None
		self._lastPos = 0
		self._sourceFile = None
		try:
			f = open(fileName, 'a')
			f.write(' ')
			f.close()
			self._sourceFile = open(fileName, 'r')
		except:
			Compiler.setError("error")
		tt = TokenType
		op = self._operators
		op["("] = Token(tt.L_PAREN, "(")
		op[")"] = Token(tt.R_PAREN, ")")
		op["["] = Token(tt.L_BRACKET, "[")
		op[","] = Token(tt.COMMA, ",")
		op[";"] = Token(tt.SEMICOLON, ";")
		op["{"] = Token(tt.L_BRACE, "{")
		op["}"] = Token(tt.R_BRACE, "}")
		op["="] = Token(tt.ASSIGN, "=")
		op["else"] = Token(tt.ELSE, "else")
		op["if"] = Token(tt.IF_WHILE, "if")
		op["while"] = Token(tt.IF_WHILE, "while")
		op["int"] = Token(tt.INT_VOID, "int")
		op["void"] = Token(tt.INT_VOID, "void")
		for rel in ['<', '<=', '==', '>', '>=', '!=']:
			op[rel] = Token(tt.REL_OP, rel)
		op["]"] = Token(tt.R_BRACKET, "]")
		op["."] = Token(tt.DOT, ".")
		op["+"] = Token(tt.ADD_OP, "+")
		op["-"] = Token(tt.ADD_OP, "-")
		op["*"] = Token(tt.MULT_OP, "*")
		op["/"] = Token(tt.MULT_OP, "/")
		
			
	def getLineNumber(self):
		return self._lineNumber
	def nextToken(self):
		try:
			tk = ""
			if self._saveToken is not None:
				tk = self._saveToken
				self._saveToken = None
			ch = self._readCharacter()
			try:
				while re.match(r"\s", ch):
					ch = self._readCharacter()
			except:
				pass
				
			if re.match("[a-zA-Z]", ch):
				tk = self._readSymbol(ch)
			elif re.match("[0-9]", ch):
				tk = self._readLiteral(ch)
			elif re.match("#", ch):
				tk = ch
				while re.match("[^;]", ch):
					tk += ch
					ch = self._readCharacter()
				if tk == "#debugon;":
					Compiler.debugOn()
				elif tk == "#debugoff;":
					Compiler.debugOff()
				elif tk == "#dump;":
					Compiler._symbols.dump()
			elif re.match("/", ch):
				pass
			elif re.match(r"[<>!=+\-\*/\(\)\{\}\[\],\.;]", ch):
				tk = ch
				ch = self._readCharacter()
				try:
					if re.match("[<>!=]=", tk + ch):
						tk += ch
				except:
					pass
				else:
					self._unreadCharacter()
				op = self._operators[tk]
				tk = Token(op.getTokenType(), op.toString())
				self._saveToken = None
			return tk
		except EOFError:
			print 'eof'
			
	def peekToken(self):
		if self._saveToken is not None:
			return self._saveToken
		else:
			self._saveToken = self.nextToken()
			return self._saveToken
    
    #private
	def _isOctalDigit(self, c):
		if c >= '0' and c <= '7':
			return True
	def _readCharacter(self):
		self.lastPos = self._sourceFile.tell()
		ch = self._sourceFile.read(1)
		if ch == '\n':
			self._lineNumber += 1
		if ch != '':
			return ch
		return -1
				
	def _readLiteral(self, firstChar):
		lit = firstChar
		next = self._readCharacter()
		while True:
			lit += next
			next = self._readCharacter()
			if re.match("\s", next) or next == -1:
				print 'wspace'
				break
		num = 0
		
		if re.match(r"0[0-7]+", lit):
			num = int(lit, 8)
		elif re.match(r"[1-9][0-9]+", lit):
			num = int(lit, 10)
		elif re.match(r"0[xX][0-9a-fA-F]+", lit):
			num = int(lit, 16)
		else:
			num = 0
		return Token(TokenType.LITERAL, str(num))
		
	def _readSymbol(self, firstChar):
		pass
	def _unreadCharacter(self):
		self._sourceFile.seek(self.lastPos)