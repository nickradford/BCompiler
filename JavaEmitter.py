from Compiler import *

class Opcode():
    ALOAD=0x19,         # load array reference from variable
    ALOAD_0=0x2a,       # load array reference from variable #0
    ALOAD_1=0x2b,       # load array reference from variable #1
    ALOAD_2=0x2c,       # load array reference from variable #2
    ALOAD_3=0x2d,       # load array reference from variable #3
    ARRAYLENGTH=0xbe,   # get length of array
    ASTORE=0x3a,        # store array reference into variable
    ASTORE_0=0x4b,      # store array reference into variable #0
    ASTORE_1=0x4c,      # store array reference into variable #1
    ASTORE_2=0x4d,      # store array reference into variable #2
    ASTORE_3=0x4e,      # store array reference into variable #3
    BIPUSH=0x10,        # push byte constant
    DUP=0x59,           # duplicate the top stack value
    DUP_X1=0x5a,        # duplicate stack top and insert 2 values down
    DUP_X2=0x5b,        # duplicate stack top, insert 3 values down
    DUP2=0x5c,          # duplicate top 2 stack values
    DUP2_x1=0x5d,       # duplicate top 2 stack values, insert 2 values down
    DUP2_x2=0x5e,       # duplicate top 2 stack values, insert 3 values down
    GETSTATIC=0xb2,     # get static field from class
    GOTO=0xa7,          # unconditional branch
    IADD=0x60,          # add integers
    IALOAD=0x2e,        # load integer from array
    IAND=0x7e,          # bool AND integers
    IASTORE=0x4f,       # store into integer array
    ICONST_M1=0x02,     # push -1 onto stack
    ICONST_0=0x03,      # push 0 onto stack
    ICONST_1=0x04,      # push 1 onto stack
    ICONST_2=0x05,      # push 2 onto stack
    ICONST_3=0x06,      # push 3 onto stack
    ICONST_4=0x07,      # push 4 onto stack
    ICONST_5=0x08,      # push 5 onto stack
    IDIV=0x6c,          # divide integers
    IF_ICMPEQ=0x9f,     # branch if equal
    IF_ICMPNE=0xa0,     # branch if not equal
    IF_ICMPLT=0xa1,     # branch if less than
    IF_ICMPGE=0xa2,     # branch if greater than or equal
    IF_ICMPGT=0xa3,     # branch if greater than
    IF_ICMPLE=0xa4,     # branch if less than or equal
    IFEQ=0x99,          # branch if zero
    IFNE=0x9a,          # branch if not zero
    IFLT=0x9b,          # branch if less than zero
    IFGE=0x9c,          # branch if greater than or equal to zero
    IFGT=0x9d,          # branch if greater than zero
    IFLE=0x9e,          # branch if less than or equal to zero
    IINC=0x84,          # increment variable by constant
    ILOAD=0x15,         # load integer from local variable
    ILOAD_0=0x1a,       # load integer from variable #0
    ILOAD_1=0x1b,       # load integer from variable #1
    ILOAD_2=0x1c,       # load integer from variable #2
    ILOAD_3=0x1d,       # load integer from variable #3
    IMUL=0x68,          # multiply integers
    INEG=0x74,          # negate integers
    INVOKEVIRTUAL=0xb6, # invoke virtual function (println)
    IOR=0x80,           # bool OR integers
    IREM=0x70,          # remainder (mod)
    ISHL=0x78,          # shift left
    ISHR=0x7a,          # shift right
    ISTORE=0x36,        # store integer into local variable
    ISTORE_0=0x3b,      # store integer into variable #0
    ISTORE_1=0x3c,      # store integer into variable #1
    ISTORE_2=0x3d,      # store integer into variable #2
    ISTORE_3=0x3e,      # store integer into variable #3
    ISUB=0x64,          # subtract integers
    IUSHR=0x7c,         # logical shift right
    IXOR=0x82,          # bool exclusive OR
    JSR=0xa8,           # jump to subroutine
    NEWARRAY=0xbc,      # create new array
    NOP=0x00,           # no operation
    POP=0x57,           # pop the stack
    POP2=0x58,          # pop top two stack values
    RET=0xa9,           # return from subroutine
    RETURN=0xb1,        # return from main program
    SIPUSH=0x11,        # push constant onto stack
    SWAP=0x5f           # swap the top two stack values	

class JavaEmitter(Compiler):
	def __init__(self):
		pass
	def chooseOp(self, longOp, shortOp, loc):
		pass
	def emit(self, op):
		pass
	def emit(self, op, ch):
		pass
	def emit(self, op, int):
		pass
	def emit(self, address, value):
		pass
	def finish(self):
		pass
	def getPC(self):
		pass
	#private
	_pc = None
	_code = None
	_opArray = None
	_opFilled = None