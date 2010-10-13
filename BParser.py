#----------------------- BParser.py -----------------------#
#
# Implemented from code provided by Dr. Lancaster
#
#
# This class parses a B program and calls the appropriate
# code generators to produce JVM Object Code.
#
#----------------------------------------------------------#

import ExpressionParser
import ParserBase
import Symbol
import Token

class BParser(Parserbase):
    #public
    def __init__(self):
        self.currentOp = None
	    self.exp = None
	    self.forwardReferences = None
	    self.loopStatus = None
	    self.nextLocation = None
	    self.nextOp = None
	    self.operand = None
	    self.scope = None
	    self.structureStack = None
	    self.suppressAdvance = None
    def compile(self, filename):
        pass
    
    #protected
    class _ForwardRef:
        #public
        reference = None
        instrLocation = None
        def __init__(self, op, loc):
            self.reference = op
            self.instrLocation = loc
    
    currentOp = None
    exp = None
    forwardReferences = None
    loopStatus = None
    nextLocation = None
    nextOp = None
    operand = None
    scope = None
    structureStack = None
    suppressAdvance = None
    
    def advance(self):
        pass
    def compileExpression(self):
        pass
    def fillAddress(self, referenceLoc, targetLoc):
        pass
    def saveForwardReference(self, symbol, address):
        pass
    
    #private
    def _compileCondition(self):
        pass
    def _fillForwardReferences(self):
        pass
    def _generate(self, currentOp, nextOp):
        pass
    # code generators
    def _AS(self):
        pass
    def _CA(self):
        pass
    def _CO(self):
        pass
    def _DE(self):
        pass
    def _DF(self):
        pass
    def _EB(self):
        pass
    def _NO(self):
        pass
    def _xx(self):
        pass
    #parsing table
    
    