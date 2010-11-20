#----------------------- BParser.py -----------------------#
#
# Implemented from code provided by Dr. Lancaster
#
#
# This class parses a B program and calls the appropriate
# code generators to produce JVM Object Code.
#
#----------------------------------------------------------#

from ExpressionParser   import *
from ParserBase         import *
from Symbol             import *
from Token              import *
from ActionTable		import *


#protected
class ForwardRef:
	#public
	def __init__(self, op, loc):
		self.reference = op
		self.instrLocation = loc
		
class Structure:
	def __init__(self, ptype):
		self.type = ptype
		self.conditionLoc = None
		self.jumpLoc = None
	
	def isOfType(self, ptype):
		if self.type == ptype:
			return True 
		else:
			return False
	

class StructureType:
	ELSE, IF, FUNCTION, MAIN, WHILE = range(5)

#public
class BParser(ParserBase):
	#public
	def __init__(self, fn):
		self.currentOp = None
		self.filename = fn
		self.bs = BScanner(self.filename)
		self.exp = ExpressionParser(self.bs)
		self.forwardReferences = []
		self.loopStatus = Status.CONTINUE
		self.nextLocation = 1
		self.nextOp = None
		self.operand = None
		self.scope = SymbolScope.GLOBAL
		self.structureStack = []
		self.suppressAdvance = False
		self.jvm = JavaEmitter()
		self.AC = ActionTable(self)
		
		#print self.currentOp, self.operand, self.nextOp, "1"
	
	#def compile(self, filename):
	#	self.bs = BScanner(filename)
	#	self.bs.debugOn()
	#	while self.nextOp.getTokenType() != TokenType.END_FILE:
	#		self.advance()
	def compile(self):
		#self.bs.debugOn()
		main = Symbol("Main", SymbolType.FORWARD_FUNCTION, SymbolScope.GLOBAL)
		self.bs._symbols.insert(main)
		
		write = Symbol("write", SymbolType.DEFINED_FUNCTION, SymbolScope.GLOBAL)
		self.bs._symbols.insert(write)
		if self.bs.debugging():
			self.bs._symbols.dump()
		self.nextOp = self.bs.nextToken()
		if self.nextOp.toString() == "void":
			self.jvm.emit3byte(Opcode.GOTO, 0)
		while self.loopStatus != Status.EXIT:
			print ".",
			self.advance()
			self._generate(self.currentOp, self.nextOp)
		self.fillForwardReferences()
		self.jvm.finish()
    
    
    
    
	
	def advance(self):
		#if self.suppressAdvance ? self.supressAdvance = False : pass
		
		
	  	if self.suppressAdvance == True:
	  		self.suppressAdvance = False
			return
		
		if self.operand != None:
			self.operand = None
		
		self.currentOp = self.nextOp
		try:
			nt = self.bs.nextToken()
		except:
			nt = Token(TokenType.END_FILE, 'EOF')
		#print self.currentOp, self.currentOp.toString(), nt, nt.toString()
		if nt == "":
			return
		if nt.getTokenType() == TokenType.END_FILE:
			self.nextOp = nt
			return
		elif nt.getTokenType() == TokenType.SYMBOL or nt.getTokenType() == TokenType.LITERAL:
			self.operand = nt
			print "OPERAND SET", self.operand.toString()
			try:
				nt = self.bs.nextToken()
			except:
				nt = Token(TokenType.END_FILE, 'EOF')
		 	
		self.nextOp = nt
			
		if self.bs.debugging():
			msg = self.currentOp.toString() + " "
			msg += self.operand.toString() + " "
			msg += self.nextOp.toString() + " "
			self.bs.showMessage(msg)
		
		
		
	
	
	def compileExpression(self):
	    self.nextOp = self.exp.compileExpression()
	def fillAddress(self, referenceLoc, targetLoc):
		targetLoc = targetLoc - referenceLoc
		self.jvm.emitFFR()
	def saveForwardReference(self, symbol, address):
		fr = ForwardRef(symbol, address)
		self.forwardReferences.append(fr)
	
	#private
	def _compileCondition(self):
		self.compileExpression()
		relop = self.bs.nextToken()
		self.compileExpression()
		relstr = relop.toString()
		if relstr == "<":
			self.jvm.emit3byte(Opcode.IF_ICMPGE, 0)	#do you just emit the i_cmp opcode? (what about the offset)
		if relstr == ">":
			self.jvm.emit3byte(Opcode.IF_ICMPLE, 0)
		if relstr == "<=":
			self.jvm.emit3byte(Opcode.IF_ICMPGT, 0)		
		if relstr == ">=":
			self.jvm.emit3byte(Opcode.IF_ICMPLT, 0)
		if relstr == "==":
			self.jvm.emit3byte(Opcode.IF_ICMPNE, 0)
		if relstr == "!=":
			self.jvm.emit3byte(Opcode.IF_ICMPEQ, 0)
		
	def fillForwardReferences(self):
	    while len(self.forwardReferences) != 0:
			ref = self.forwardReferences.pop()
			self.fillAddress(ref.instrLocation, ref.reference.getAddress())
			
	def _generate(self, cOp, nOp):
		cOpTT = cOp.getTokenType()
		nOpTT = nOp.getTokenType()
		if  cOpTT >= TokenType.END_FILE or nOpTT >= TokenType.END_FILE:
			self._xx()
		else:
			self.AC.cono[cOpTT][nOpTT]()
	
	# code generators
	# ASsignment
	def _AS(self):
		if self.nextOp == TokenType.L_BRACKET:
			sym = self.symbols.get(operand.toString())
			self/jvm.chooseOp(ALOAD, ALOAD_1, sym.getAddress())
			sub = self.compileExpression()
			val = self.compileExpression()
			self.jvm.emit(IASTORE)

		else:
			sym = self.symbols.get(operand.toString())
			val = self.compileExpression()
			self.jvm.chooseOp(ISTORE, ISTORE_0, sym.getAddress())

	
	# CAll function		
	def _CA(self):
		print "calling a function"
		if self.operand.toString() == "write":
			print "calling the write function"
			self.jvm.emit3byte(Opcode.GETSTATIC, 6)
			self.compileExpression()
			self.jvm.emit3byte(Opcode.INVOKEVIRTUAL, 7)
		else:
			if not self.symbols.defined(operand.toString()):
				sym = Symbol(self.operand.toString(), SymbolType.FORWARD_FUNCTION, self.scope)
				self.symbols.insert(sym)
			
			sym = self.symbols.get(self.operand.toString())
			if sym.getSymbolType() == SymbolType.FORWARD_FUNCTION:
				self.saveForwardReference(sym, self.jvm.getPC())
				self.jvm.emit3byte(Opcode.GOTO, 0) #jsr
			elif sym.getSymbolType() == SymbolType.DEFINED_FUNCTION:
				self.jvm.emit3byte(Opcode.GOTO, sym.getAddress() - self.jvm.getPC()) #jsr
		
	# COndition
	def _CO(self):
		if self.nextOp.toString() == "if":
			struc = Structure(StructureType.IF)
			self.compileCondition()
			struc.jumpLoc = self.jvm.getPC() - 3
			self.structureStack.append(struc)
		elif self.nextOp.toString() == "while":
			struc = Structure(StructureType.WHILE)
			struc.conditionLoc = self.jvm.getPC()
			self.structureStack.append(struc)
			self.compileCondition()
			struc.jumpLoc = self.jvm.getPC() - 3			
		
		pass #save position of conditional jump at end of the cond as jumpLoc (pc - 3)
	
	# DEclaration
	def _DE(self):
		self.supressAdvance = True
		print "declaring a variable..."
		while self.nextOp.toString() != ";":
			self.advance()
			sym = Symbol(self.operand.toString(), None, self.scope)
			sym.setAddress(self.nextLocation)
			if self.nextOp.toString() == "[":
				sym.setSymbolType(SymbolType.ARRAY)
				self.advance() # co = '[', no = ']'
				self.pushConstant(self.operand)
				sub = self.operand
				self.jvm.emit2byte(Opcode.NEWARRAY, 10)
				sym.setAddress(self.nextLocation)
				self.jvm.chooseOp(Opcode.ASTORE, Opcode.ASTORE_0, sym.getAddress())
				self.advance() # co = ']', no = ('=' | ';')
				if self.nextOp.toString() == "=":
					self.advance() # co = '=', no = '{'
					if self.nextOp.toString() != "{":
						self.setError("Syntax Error: Missing { after = ");
					
					self.advance() #co = '{', no = ','
					arr = []
					while self.nextOp.toString() != "}":
						arr.append(self.operand)
						self.advance() 
					if len(arr) > sub:
						self.setError("Syntax Error: Array Subscript exceeded")
					else:
						i = 0
						for val in arr:
							self.jvm.chooseOp(Opcode.ALOAD, Opcode.ALOAD_0, sym.getAddress())
							self.pushConstant(i)
							self.pushConstant(val)
							self.jvm.emit1byte(Opcode.IASTORE)
							i += 1							
							
			else: #if not an array
				sym.setSymbolType(SymbolType.VARIABLE)
				sym.setAddress(self.nextLocation)
				self.advance()
				self.pushConstant(self.operand)
				self.jvm.chooseOp(Opcode.ISTORE, Opcode.ISTORE_0, sym.getAddress())
				print "declared a variable"
				
				#do variable declaration things
			self.bs._symbols.insert(sym)
			self.nextLocation += 1
		try:	
			if self.scope == SymbolScope.GLOBAL and self.bs.peekToken().toString() != "int":
				self.jvm.emit3byte(Opcode.JSR, 0)
		except:			
			pass
	
	# Define Function
	def _DF(self):
		self.scope = SymbolScope.LOCAL
		if self.bs._symbols.defined(self.operand):
			sym = self.bs._symbols.get(self.operand)
			sym.setSymbolType(SymbolType.DEFINED_FUNCTION)
		else:
			sym = Symbol(self.operand.toString(), SymbolType.DEFINED_FUNCTION, SymbolScope.GLOBAL)
		sym.setAddress(self.jvm.getPC())
		
		if sym.toString() == "Main":
			print "Main Function"
			struct = Structure(StructureType.MAIN)
		else:
			struct = Structure(StructureType.FUNCTION)
		print self.structureStack
		self.structureStack.append(struct)
		print "structure pushed"
	
	# End Block
	def _EB(self):
		struct = self.structureStack.pop()
		if struct.isOfType(StructureType.ELSE):
			self.fillAddress() #not done
		elif struct.isOfType(StructureType.IF):
			if self.bs.peekToken().toString() == "else":
				pstru = Structure(StructureType.ELSE)
				pstru.jumpLoc = self.jvm.getPC()
				#emit code to jump past false part
			self.fillAddress()
		elif struct.isOfType(StructureType.FUNCTION):
			self.scope = SymbolScope.GLOBAL
			self._symbols.clearLocalTable()
			#generate code to save the return address in loc0 and emit instruction
			#return to the calling point
			#emit ret
			if self.bs.peekToken().getTokenType() == TokenType.END_FILE:
				self.loopStatus = Status.EXIT
		elif struct.isOfType(StructureType.MAIN):
			self.scope = SymbolScope.GLOBAL
			self._symbols.clearLocalTable()
			#emit the instruction to terminate the program
			#emit return
			if self.bs.peekToken().getTokenType() == TokenType.END_FILE:
				self.loopStatus = Status.EXIT
		del struct
	# No Op
	def _NO(self):
		#derp
		pass
	
	# Error
	def _xx(self):
		pass
#parsing table
    
    