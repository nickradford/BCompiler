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
			self.setError("error")
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
		tk = ""
		
		if self._saveToken != None:
			tk = self._saveToken
			self._saveToken = None
			return tk
		ch = self._readCharacter()
		try:
			while re.match(r"\s", ch):
				ch = self._readCharacter()
		except:
			pass
			
		if ch == "":
			print "Empty string"
		
		if re.match("[a-zA-Z]", ch):
			tk = self._readSymbol(ch)
		elif re.match("[0-9]", ch):
			tk = self._readLiteral(ch)
		elif re.match("#", ch):
			tk = ch
			while re.match("[^;]", ch):
				ch = self._readCharacter()
				tk += ch
			if tk == "#debugon;":
				print "debugging"
				self.debugOn()
				
			elif tk == "#debugoff;":
				self.debugOff()
			elif tk == "#dump;":
				self._symbols.dump()
			elif tk == "#EOF;":
				return Token(TokenType.END_FILE, 'EOF')
			return self.nextToken();
		elif re.match(r"[<>!=+\-\*\(\)\{\}\[\],\.;]", ch):
			tk = ch
			ch = self._readCharacter()
			if re.match("[<>!=]=", tk + ch):
				tk += ch
			else:
				self._unreadCharacter()
			op = self._operators[tk]
			tk = Token(op.getTokenType(), op.toString())
			print tk.toString()
		elif re.match("/", ch):
			tk = ch
			ch = self._readCharacter()
			if re.match("//", tk + ch):
				next = self._readCharacter()
				while next != '\n':
					next = self._readCharacter()
				tk = self.nextToken()
			elif re.match(r"/\*", tk +ch):
				this = self._readCharacter()
				next = self._readCharacter()
				while this != '*':
					this = next
					next = self._readCharacter()
				tk = self.nextToken()		
			else:
				self._unreadCharacter()
				op = self._operators[tk]
				tk = Token(op.getTokenType(), op.toString())
		elif re.match("'", ch):
			ch = self._readCharacter()
			throwaway = self._readCharacter()
			tk = Token(TokenType.LITERAL, str(ord(ch)))
		else:
			print "EOF-EOF-EOF"
			tk = self._readEOF()
		
		self._saveToken = None
		
		if tk != "" and tk != None:
			return tk
		else:
			None
			
	def peekToken(self):
		if self._saveToken == None:
			self._saveToken = self.nextToken()
		return self._saveToken
    
    #private
	def _isOctalDigit(self, c):
		if c >= '0' and c <= '7':
			return True
	def _readCharacter(self):
		self._lastPos = self._sourceFile.tell()
		ch = self._sourceFile.read(1)
		if ch == '\n':
			self._lineNumber += 1
		if ch != '':
			return ch
		return -1
				
	def _readLiteral(self, firstChar):
		lit = firstChar
		next = self._readCharacter()
		while re.match(r"[0-9xXa-fA-F]", next):
			lit += next
			next = self._readCharacter()
		
		self._unreadCharacter()
			
		num = 0
		if re.match(r"0[xX][0-9a-fA-F]+", lit):
			literal = lit
			lit = literal[2:]
			num = int(lit, 16)
		elif re.match(r"0[0-7]+", lit):
			num = int(lit, 8)
		elif re.match(r"[1-9][0-9]*", lit):
			num = int(lit, 10)
		else:
			num = 0
			#should return error
		return Token(TokenType.LITERAL, str(num))
		
	def _readSymbol(self, firstChar):
		tk = firstChar
		next = self._readCharacter()
		while re.match("[a-zA-Z0-9]", next):
			tk += next
			next = self._readCharacter()
		if tk in self._operators:
			res = self._operators[tk]
			tk = Token(res.getTokenType(), res.toString())
		else:
			tk = Token(TokenType.SYMBOL, tk)
		self._unreadCharacter()
		return tk
	def _readEOF(self):
		tk = Token(TokenType.END_FILE, 'EOF')
		return tk
	def _unreadCharacter(self):
		self._sourceFile.seek(self._lastPos)