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
			self._sourceFile = open(fileName)
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
				while re.match("\s", ch):
					ch = self._readCharacter()
			except:
				print "error... \'" + ch + "\' is not okay"
				
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
			elif re.match("'", ch):
				pass
			elif re.match("/", ch):
				pass
			elif re.match("[<>!=+\-*/(){}\[\],\.;]", ch):
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
			return tk
			
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
		if ch != '':
			return ch
		else:
			pass
	def _readLiteral(self, firstChar):
		next = self._readCharacter()
		if int(firstChar) != 0:
			base = 10
		elif int(firstChar) == 0:
			if next == 'x':
				base = 16
				next = self._readCharacter()
			else:
				base = 8
		
		val = int(firstChar)
		power = 0
		try:
			while re.match("\d", next):
				val *= base
				val += int(next)
				next = self._readCharacter()
		except:
			pass
		self._unreadCharacter();
		return Token(TokenType.LITERAL, Compiler.long2string(val))
		
	def _readSymbol(self, firstChar):
		pass
	def _unreadCharacter(self):
		self._sourceFile.seek(self.lastPos)