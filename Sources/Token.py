#------------------------ Token.py ---------------------------------#
#
# Implemented from code provided by Dr. Lancaster
#
#
# This class represents the tokens that are returned by the scanner.
# This file also defines the enum TokenType.
#
#-------------------------------------------------------------------#

class TokenType:
    L_PAREN = 0     # (
    R_PAREN = 1     # )
    L_BRACKET = 2   # [
    COMMA = 3       # ,
    SEMICOLON = 4   # ;
    L_BRACE = 5     # {
    R_BRACE = 6     # }
    ASSIGN = 7      # =
    ELSE = 8        # else
    IF_WHILE = 9    # if, while
    INT_VOID = 10   # int, void
    END_FILE = 11   # end-of-file
    ADD_OP = 12     # +, -
    MULT_OP = 13    # *, /
    REL_OP = 14     # <, <=, ==, >, >=, !=
    R_BRACKET = 15  # ]
    DOT = 16        # .
    LITERAL = 17    # numeric literal
    SYMBOL = 18     # symbol  


    

class Token:
    _lexeme = None
    _type = None
    def __init__(self, tt, lexeme):
        self._lexeme = lexeme
        self._tokenType = tt
    
    def getTokenType(self):
        return self._tokenType
    
    def toString(self):
        return self._lexeme
        
