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
		self.jvm = self.exp.jvm
		self.AC = ActionTable(self)
		self.advances = 0
		
		#print self.currentOp, self.operand, self.nextOp, "1"
	
	#def compile(self, filename):
	#	self.bs = BScanner(filename)
	#	self.bs.debugOn()
	#	while self.nextOp.getTokenType() != TokenType.END_FILE:
	#		self.advance()
	def compile(self):
		#self.bs.debugOn()
		#try:
			main = Symbol("Main", SymbolType.FORWARD_FUNCTION, SymbolScope.GLOBAL)
			self.bs._symbols.insert(main)
			
			write = Symbol("write", SymbolType.DEFINED_FUNCTION, SymbolScope.GLOBAL)
			self.bs._symbols.insert(write)
			if self.bs.debugging():
				self.bs._symbols.dump()
			self.nextOp = self.bs.nextToken()
			print self.nextOp
			if self.nextOp.toString() == "void":
				sym = self.bs._symbols.get("Main")
				self.saveForwardReference(sym, self.jvm.getPC())
				self.jvm.emit3byte(Opcode.GOTO, 0)
			while self.loopStatus != Status.EXIT:
				print ".",
				self.advance()
				self._generate(self.currentOp, self.nextOp)
			self.fillForwardReferences()
			self.jvm.finish()
		#except:
			#self._debugFile.close()
			#pass
    
    
    
    
	
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
		
		print self.advances, self.currentOp.toString(), self.operand, self.nextOp.toString()
		self.advances += 1
	  #try:	
	  #	if self.bs.debugging():
	  #		msg = self.currentOp.toString() + " "
	  #		msg += self.operand.toString() + " "
	  #		msg += self.nextOp.toString() + " "
	  #		self.bs.showMessage(msg)
	  #except:
	  #	self.bs.showMessage("")
	
	def compileExpression(self):
		print "compiling expression"
		self.nextOp = self.exp.compileExpression()
		
	def fillAddress(self, referenceLoc, targetLoc):
		targetLoc = targetLoc - referenceLoc
		self.jvm.emitFFR(referenceLoc + 1, targetLoc)
		
	def saveForwardReference(self, symbol, address):
		fr = ForwardRef(symbol, address)
		print fr.reference.toString(), " SAVE FR:::"
		self.forwardReferences.append(fr)
		
   	def fillForwardReferences(self):
		while len(self.forwardReferences) != 0:
			ref = self.forwardReferences.pop()
			self.fillAddress(ref.instrLocation, ref.reference.getAddress())	
	#private
	def _compileCondition(self):
		self.compileExpression()
		relop = self.nextOp
		self.compileExpression()
		relstr = relop.toString()
		print "RELOP!!!1 :", relop
		print "RELSTRING!!!", relstr
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
		print "AS()"
		print self.nextOp.toString(), "ASSIGNMENT&*&*&"
		if self.nextOp.getTokenType() == TokenType.L_BRACKET:
			sym = self.bs._symbols.get(self.operand.toString())
			self.jvm.chooseOp(Opcode.ALOAD, Opcode.ALOAD_0, sym.getAddress())
			self.compileExpression()
			self.advance()
			self.compileExpression()
			self.jvm.emit1byte(Opcode.IASTORE)

		else:
			sym = self.bs._symbols.get(self.operand.toString())
			val = self.compileExpression()
			print self.currentOp.toString(), self.operand.toString(), self.nextOp.toString()
			self.jvm.chooseOp(Opcode.ISTORE, Opcode.ISTORE_0, sym.getAddress())

	
	# CAll function		
	def _CA(self):
		print "CA()"
		print "calling a function: ", self.currentOp.toString(), self.operand.toString(), self.nextOp.toString()
		if self.operand.toString() == "write":
			print "calling the write function"
			self.jvm.emit3byte(Opcode.GETSTATIC, 6)
			self.compileExpression()
			self.jvm.emit3byte(Opcode.INVOKEVIRTUAL, 7)
		else:
			if self.bs._symbols.defined(self.operand.toString()) == False:
				print "function not defined"
				sym = Symbol(self.operand.toString(), SymbolType.FORWARD_FUNCTION, self.scope)
				self.bs._symbols.insert(sym)
			
			sym = self.bs._symbols.get(self.operand.toString())
			if sym.getSymbolType() == SymbolType.FORWARD_FUNCTION:
				self.saveForwardReference(sym, self.jvm.getPC())
				self.jvm.emit3byte(Opcode.JSR, 0) #jsr
			elif sym.getSymbolType() == SymbolType.DEFINED_FUNCTION:
				self.jvm.emit3byte(Opcode.JSR, sym.getAddress() - self.jvm.getPC()) #jsr
		
	# COndition
	def _CO(self):
		print "CO()"
		if self.currentOp.toString() == "if":
			struc = Structure(StructureType.IF)
			self._compileCondition()
			struc.jumpLoc = self.jvm.getPC() - 3
			self.structureStack.append(struc)
			print "Pushed IF Structure"
		elif self.currentOp.toString() == "while":
			struc = Structure(StructureType.WHILE)
			struc.conditionLoc = self.jvm.getPC()
			self._compileCondition()
			struc.jumpLoc = self.jvm.getPC() - 3
			self.structureStack.append(struc)	
			print "Pushed WHILE structure"		
		
		pass #save position of conditional jump at end of the cond as jumpLoc (pc - 3)
	
	# DEclaration
	def _DE(self):
		print "DE()"
		self.suppressAdvance = True
		print "declaring a variable..."
		while self.nextOp.toString() != ";":
			print self.operand.toString(), "SYMBOL!!!"
			sym = Symbol(self.operand.toString(), None, self.scope)
			self.advance()
			sym.setAddress(self.nextLocation)
			if self.nextOp.toString() == "[":
				sym.setSymbolType(SymbolType.ARRAY)
				self.advance() # co = '[', no = ']'
				self.pushConstant(self.operand)
				size = self.operand.toString()
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
					while self.nextOp.toString() != ";":
						print "Array Declaration :", self.operand.toString()
						arr.append(self.operand)
						self.advance() 
					if len(arr) > size:
						self.setError("Syntax Error: Array Subscript exceeded")
					else:
						i = 0
						for val in arr:
							self.jvm.chooseOp(Opcode.ALOAD, Opcode.ALOAD_0, sym.getAddress())
							self.pushConstantInt(i)
							self.pushConstant(val)
							self.jvm.emit1byte(Opcode.IASTORE)
							i += 1							
							
			else: #if not an array
				sym.setSymbolType(SymbolType.VARIABLE)
				#sym.setAddress(self.nextLocation)
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
		print "DF()"
		self.scope = SymbolScope.LOCAL
		if self.bs._symbols.defined(self.operand.toString()):
			sym = self.bs._symbols.get(self.operand.toString())
			sym.setSymbolType(SymbolType.DEFINED_FUNCTION)
		else:
			sym = Symbol(self.operand.toString(), SymbolType.DEFINED_FUNCTION, SymbolScope.GLOBAL)
			self.bs._symbols.insert(sym)
		sym.setAddress(self.jvm.getPC())
		
		if sym.toString() == "Main":
			print "Main Function Definition"
			struct = Structure(StructureType.MAIN)
		else:
			struct = Structure(StructureType.FUNCTION)
			print "Function Definition"
		self.structureStack.append(struct)
		print self.structureStack
		print len(self.structureStack), ": structure pushed, "
	
	# End Block
	def _EB(self):
		print "EB()"
		#print "END BLOCK: ", self.currentOp.toString(), self.operand.toString(), self.nextOp.toString()
		struct = self.structureStack.pop()
		if struct.isOfType(StructureType.ELSE):
			self.fillAddress() #not done
		elif struct.isOfType(StructureType.IF):
			if self.bs.peekToken().toString() == "else":
				pstru = Structure(StructureType.ELSE)
				pstru.jumpLoc = self.jvm.getPC()
				self.structureStack.append(pstru)
	    		#emit code to jump past false part
			self.jvm.emitFFR(struct.jumpLoc + 1, self.jvm.getPC() - struct.jumpLoc)
		elif struct.isOfType(StructureType.WHILE):
			self.jvm.emit3byte(Opcode.GOTO, struct.conditionLoc - self.jvm.getPC())
			self.fillAddress(struct.jumpLoc, self.jvm.getPC())
		elif struct.isOfType(StructureType.FUNCTION):
			self.scope = SymbolScope.GLOBAL
			self.bs._symbols.clearLocalTable()
			#generate code to save the return address in loc0 and emit instruction
			#return to the calling point
			self.jvm.emit1byte(Opcode.ASTORE_0)
			self.jvm.emit2byte(Opcode.RET, 0)
			if self.bs.peekToken().getTokenType() == TokenType.END_FILE:
				self.loopStatus = Status.EXIT
		elif struct.isOfType(StructureType.MAIN):
			self.scope = SymbolScope.GLOBAL
			self.bs._symbols.clearLocalTable()
			#emit the instruction to terminate the program
			#emit return
			self.jvm.emit1byte(Opcode.RETURN)
			print self.bs.peekToken().toString(), "PEEK TOKEN^@#*&^@#*^"
			if self.bs.peekToken().getTokenType() == TokenType.END_FILE:
				self.loopStatus = Status.EXIT
				
		del struct
		#self.jvm.emit1byte(Opcode.RETURN)
		#self.loopStatus = Status.EXIT
	
	# No Op
	def _NO(self):
		print "NO()"
		pass
	
	# Error
	def _xx(self):
		print "XX()"
		pass
#parsing table
    
    