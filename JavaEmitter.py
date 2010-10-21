from Compiler import *
from struct import *
import binascii

class Opcode():
    ALOAD=0x19         # load array reference from variable
    ALOAD_0=0x2a       # load array reference from variable #0
    ALOAD_1=0x2b       # load array reference from variable #1
    ALOAD_2=0x2c       # load array reference from variable #2
    ALOAD_3=0x2d       # load array reference from variable #3
    ARRAYLENGTH=0xbe   # get length of array
    ASTORE=0x3a        # store array reference into variable
    ASTORE_0=0x4b      # store array reference into variable #0
    ASTORE_1=0x4c      # store array reference into variable #1
    ASTORE_2=0x4d      # store array reference into variable #2
    ASTORE_3=0x4e      # store array reference into variable #3
    BIPUSH=0x10        # push byte constant
    DUP=0x59           # duplicate the top stack value
    DUP_X1=0x5a        # duplicate stack top and insert 2 values down
    DUP_X2=0x5b        # duplicate stack top insert 3 values down
    DUP2=0x5c          # duplicate top 2 stack values
    DUP2_x1=0x5d       # duplicate top 2 stack values insert 2 values down
    DUP2_x2=0x5e       # duplicate top 2 stack values insert 3 values down
    GETSTATIC=0xb2     # get static field from class
    GOTO=0xa7          # unconditional branch
    IADD=0x60          # add integers
    IALOAD=0x2e        # load integer from array
    IAND=0x7e          # bool AND integers
    IASTORE=0x4f       # store into integer array
    ICONST_M1=0x02     # push -1 onto stack
    ICONST_0=0x03      # push 0 onto stack
    ICONST_1=0x04      # push 1 onto stack
    ICONST_2=0x05      # push 2 onto stack
    ICONST_3=0x06      # push 3 onto stack
    ICONST_4=0x07      # push 4 onto stack
    ICONST_5=0x08      # push 5 onto stack
    IDIV=0x6c          # divide integers
    IF_ICMPEQ=0x9f     # branch if equal
    IF_ICMPNE=0xa0     # branch if not equal
    IF_ICMPLT=0xa1     # branch if less than
    IF_ICMPGE=0xa2     # branch if greater than or equal
    IF_ICMPGT=0xa3     # branch if greater than
    IF_ICMPLE=0xa4     # branch if less than or equal
    IFEQ=0x99          # branch if zero
    IFNE=0x9a          # branch if not zero
    IFLT=0x9b          # branch if less than zero
    IFGE=0x9c          # branch if greater than or equal to zero
    IFGT=0x9d          # branch if greater than zero
    IFLE=0x9e          # branch if less than or equal to zero
    IINC=0x84          # increment variable by constant
    ILOAD=0x15         # load integer from local variable
    ILOAD_0=0x1a       # load integer from variable #0
    ILOAD_1=0x1b       # load integer from variable #1
    ILOAD_2=0x1c       # load integer from variable #2
    ILOAD_3=0x1d       # load integer from variable #3
    IMUL=0x68          # multiply integers
    INEG=0x74          # negate integers
    INVOKEVIRTUAL=0xb6 # invoke virtual function (println)
    IOR=0x80           # bool OR integers
    IREM=0x70          # remainder (mod)
    ISHL=0x78          # shift left
    ISHR=0x7a          # shift right
    ISTORE=0x36        # store integer into local variable
    ISTORE_0=0x3b      # store integer into variable #0
    ISTORE_1=0x3c      # store integer into variable #1
    ISTORE_2=0x3d      # store integer into variable #2
    ISTORE_3=0x3e      # store integer into variable #3
    ISUB=0x64          # subtract integers
    IUSHR=0x7c         # logical shift right
    IXOR=0x82          # bool exclusive OR
    JSR=0xa8           # jump to subroutine
    NEWARRAY=0xbc      # create new array
    NOP=0x00           # no operation
    POP=0x57           # pop the stack
    POP2=0x58          # pop top two stack values
    RET=0xa9           # return from subroutine
    RETURN=0xb1        # return from main program
    SIPUSH=0x11        # push constant onto stack
    SWAP=0x5f           # swap the top two stack values	

class JavaEmitter(Compiler):
	def __init__(self):
		
		self._opFilled = False
		
		self._code = list()
		self._code = [
		    '\xca','\xfe','\xba','\xbe','\x00','\x03','\x00','\x2d',
		    '\x00','\x18','\x07','\x00','\x11','\x07','\x00','\x12',
		    '\x07','\x00','\x13','\x07','\x00','\x17','\x0a','\x00',
		    '\x02','\x00','\x08','\x09','\x00','\x03','\x00','\x09',
		    '\x0a','\x00','\x01','\x00','\x0a','\x0c','\x00','\x0e',
		    '\x00','\x0b','\x0c','\x00','\x15','\x00','\x10','\x0c',
		    '\x00','\x16','\x00','\x0c','\x01','\x00','\x03','\x28',
		    '\x29','\x56','\x01','\x00','\x04','\x28','\x49','\x29',
		    '\x56','\x01','\x00','\x16','\x28','\x5b','\x4c','\x6a',
		    '\x61','\x76','\x61','\x2f','\x6c','\x61','\x6e','\x67',
		    '\x2f','\x53','\x74','\x72','\x69','\x6e','\x67','\x3b',
		    '\x29','\x56','\x01','\x00','\x06','\x3c','\x69','\x6e',
		    '\x69','\x74','\x3e','\x01','\x00','\x04','\x43','\x6f',
		    '\x64','\x65','\x01','\x00','\x15','\x4c','\x6a','\x61',
		    '\x76','\x61','\x2f','\x69','\x6f','\x2f','\x50','\x72',
		    '\x69','\x6e','\x74','\x53','\x74','\x72','\x65','\x61',
		    '\x6d','\x3b','\x01','\x00','\x13','\x6a','\x61','\x76',
		    '\x61','\x2f','\x69','\x6f','\x2f','\x50','\x72','\x69',
		    '\x6e','\x74','\x53','\x74','\x72','\x65','\x61','\x6d',
		    '\x01','\x00','\x10','\x6a','\x61','\x76','\x61','\x2f',
		    '\x6c','\x61','\x6e','\x67','\x2f','\x4f','\x62','\x6a',
		    '\x65','\x63','\x74','\x01','\x00','\x10','\x6a','\x61',
		    '\x76','\x61','\x2f','\x6c','\x61','\x6e','\x67','\x2f',
		    '\x53','\x79','\x73','\x74','\x65','\x6d','\x01','\x00',
		    '\x04','\x6d','\x61','\x69','\x6e','\x01','\x00','\x03',
		    '\x6f','\x75','\x74','\x01','\x00','\x07','\x70','\x72',
		    '\x69','\x6e','\x74','\x6c','\x6e','\x01','\x00','\x03',
		    '\x72','\x75','\x6e','\x00','\x21','\x00','\x04','\x00',
		    '\x02','\x00','\x00','\x00','\x00','\x00','\x02','\x00',
		    '\x01','\x00','\x0e','\x00','\x0b','\x00','\x01','\x00',
		    '\x0f','\x00','\x00','\x00','\x11','\x00','\x01','\x00',
		    '\x01','\x00','\x00','\x00','\x05','\x2a','\xb7','\x00',
		    '\x05','\xb1','\x00','\x00','\x00','\x00','\x00','\x09',
		    '\x00','\x14','\x00','\x0d','\x00','\x01','\x00','\x0f',
		    '\x00','\x00','\x00','\xFF', # attribute length
		    '\x00','\x40',               # max stack length
		    '\x01','\x00',               # max local variables
		    '\x00','\x00','\x00','\xFF'  # code length
		]
		
		self._pc = 0x11c;
		if self._opFilled:
			return
		
		self._opFilled = True;
		self._opArray = list();
		for val in range(0, 191):
			self._opArray.append("xx")
			
		self._opArray[Opcode.ALOAD] = "aload";
		self._opArray[Opcode.ALOAD_0] = "aload_0";
		self._opArray[Opcode.ALOAD_1] = "aload_1";
		self._opArray[Opcode.ALOAD_2] = "aload_2";
		self._opArray[Opcode.ALOAD_3] = "aload_3";
		self._opArray[Opcode.ASTORE] = "astore";
		self._opArray[Opcode.ASTORE_0] = "astore_0";
		self._opArray[Opcode.ASTORE_1] = "astore_1";
		self._opArray[Opcode.ASTORE_2] = "astore_2";
		self._opArray[Opcode.ASTORE_3] = "astore_3";
		self._opArray[Opcode.BIPUSH] = "bipush";
		self._opArray[Opcode.DUP] = "dup";
		self._opArray[Opcode.DUP_X1] = "dup_x1";
		self._opArray[Opcode.DUP_X2] = "dup_x2";
		self._opArray[Opcode.DUP2] = "dup2";
		self._opArray[Opcode.DUP2_x1] = "dup2_x1";
		self._opArray[Opcode.DUP2_x2] = "dup2_x2";
		self._opArray[Opcode.GETSTATIC] = "getstatic";
		self._opArray[Opcode.GOTO] = "goto";
		self._opArray[Opcode.IADD] = "iadd";
		self._opArray[Opcode.IALOAD] = "iaload";
		self._opArray[Opcode.IAND] = "iand";
		self._opArray[Opcode.IASTORE] = "iastore";
		self._opArray[Opcode.ICONST_M1] = "iconst_m1";
		self._opArray[Opcode.ICONST_0] = "iconst_0";
		self._opArray[Opcode.ICONST_1] = "iconst_1";
		self._opArray[Opcode.ICONST_2] = "iconst_2";
		self._opArray[Opcode.ICONST_3] = "iconst_3";
		self._opArray[Opcode.ICONST_4] = "iconst_4";
		self._opArray[Opcode.ICONST_5] = "iconst_5";
		self._opArray[Opcode.IDIV] = "idiv";
		self._opArray[Opcode.IF_ICMPEQ] = "if_icmpeq";
		self._opArray[Opcode.IF_ICMPNE] = "if_icmpne";
		self._opArray[Opcode.IF_ICMPLT] = "if_icmplt";
		self._opArray[Opcode.IF_ICMPGE] = "if_icmpge";
		self._opArray[Opcode.IF_ICMPGT] = "if_icmpgt";
		self._opArray[Opcode.IF_ICMPLE] = "if_icmple";
		self._opArray[Opcode.IFEQ] = "ifeq";
		self._opArray[Opcode.IFNE] = "ifne";
		self._opArray[Opcode.IFLT] = "iflt";
		self._opArray[Opcode.IFGE] = "ifge";
		self._opArray[Opcode.IFGT] = "ifgt";
		self._opArray[Opcode.IFLE] = "ifle";
		self._opArray[Opcode.IINC] = "iinc";
		self._opArray[Opcode.ILOAD] = "iload";
		self._opArray[Opcode.ILOAD_0] = "iload_0";
		self._opArray[Opcode.ILOAD_1] = "iload_1";
		self._opArray[Opcode.ILOAD_2] = "iload_2";
		self._opArray[Opcode.ILOAD_3] = "iload_3";
		self._opArray[Opcode.IMUL] = "imul";
		self._opArray[Opcode.INEG] = "ineg";
		self._opArray[Opcode.INVOKEVIRTUAL] = "invokevirtual";
		self._opArray[Opcode.IOR] = "ior";
		self._opArray[Opcode.IREM] = "irem";
		self._opArray[Opcode.ISHL] = "ishl";
		self._opArray[Opcode.ISHR] = "ishr";
		self._opArray[Opcode.ISTORE] = "istore";
		self._opArray[Opcode.ISTORE_0] = "istore_0";
		self._opArray[Opcode.ISTORE_1] = "istore_1";
		self._opArray[Opcode.ISTORE_2] = "istore_2";
		self._opArray[Opcode.ISTORE_3] = "istore_3";
		self._opArray[Opcode.ISUB] = "isub";
		self._opArray[Opcode.IUSHR] = "iushr";
		self._opArray[Opcode.IXOR] = "ixor";
		self._opArray[Opcode.JSR] = "jsr";
		self._opArray[Opcode.NEWARRAY] = "newarray";
		self._opArray[Opcode.NOP] = "nop";
		self._opArray[Opcode.POP] = "pop";
		self._opArray[Opcode.POP2] = "pop2";
		self._opArray[Opcode.RET] = "ret";
		self._opArray[Opcode.RETURN] = "return";
		self._opArray[Opcode.SIPUSH] = "sipush";
		self._opArray[Opcode.SWAP] = "swap";
		
	def chooseOp(self, longOp, shortOp, loc):
		pass
		
	def emit1byte(self, op):
		if self.debugging():
			dbout = str(hex(self._pc)) + ": \t" + self._opArray[op] + "  " + str(hex(op)) + "\n"
			self.showMessage(dbout)

		self.add(op)
		
		self._pc += 1
	
	def emit2byte(self, op, param):
		b1 = param & 0xFF
		if self.debugging():
			dbout = str(hex(self._pc)) + ": \t" + self._opArray[op] + "  " + str(hex(op)) + "  " + str(hex(b1)) + "\n"
			self.showMessage(dbout)
		
		self.add(op)
		self._pc += 1
		self.add(b1)
		self._pc += 1
		
	def emit3byte(self, op, param):
		b1 = (param >> 8) & 0xFF
		b2 = param & 0xFF
		if self.debugging():
			dbout = str(hex(self._pc)) + ": \t" + self._opArray[op] + "  " + str(hex(op)) + "  " + str(hex(b1)) + "  " + str(hex(b2)) + "\n"
			self.showMessage(dbout)
		
		self.add(op)
		self._pc += 1
		self.add(b1)
		self._pc += 1
		self.add(b2)
		self._pc += 1
		
		
	def finish(self):
		codeLength = self._pc - 0x11c
		attrLength = codeLength + 12
		if attrLength >= 0x10000:
			self.setError("Programm to large to compile")
		
		self._code[0x11a] = pack('B',(codeLength >> 8) & 0xFF)
		self._code[0x11b] = pack('B',codeLength & 0xFF)
		self._code[0x112] = pack('B',(attrLength >> 8) & 0xFF)
		self._code[0x113] = pack('B',attrLength & 0xFF)
		
		for val in range(6):
			self.add(0x00)
		
		binaryFile = open("run.class", 'wb')
		
		for bit in self._code:
			binaryFile.write(bit)
			
			
		binaryFile.close()

		
	def add(self, op):
		hexop = pack('B', op)
		self._code.append(hexop)
		
	def getPC(self):
		pass
	#private