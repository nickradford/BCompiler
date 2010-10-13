from BParser import *

class ActionTable():
	def __init__(self):
		bp = BParser
		self.cono =  [
	    #           ** N E X T   O P **
	    #                                                                   IF    INT
	    #    (      )      [      ,      ;      {      }      =    ELSE  WHILE   VOID
	    [bp._xx,bp._NO,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx], # (         C
	    [bp._xx,bp._xx,bp._xx,bp._xx,bp._NO,bp._NO,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx], # )         U
	    [bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx], # [         R
	    [bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx], # ,         R
	    [bp._CA,bp._xx,bp._AS,bp._xx,bp._xx,bp._xx,bp._EB,bp._AS,bp._xx,bp._NO,bp._NO], # ;         E
	    [bp._CA,bp._xx,bp._AS,bp._xx,bp._xx,bp._xx,bp._xx,bp._AS,bp._xx,bp._NO,bp._NO], # {         N
	    [bp._CA,bp._xx,bp._AS,bp._xx,bp._xx,bp._xx,bp._EB,bp._AS,bp._NO,bp._NO,bp._NO], # }         T
	    [bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx], # =
	    [bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._NO,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx], # ELSE      O
	    [bp._CO,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx,bp._xx], # IF,WHILE  P
	    [bp._DF,bp._xx,bp._DE,bp._DE,bp._DE,bp._xx,bp._xx,bp._DE,bp._xx,bp._xx,bp._xx]]  # INT,VOID
	    #                                                                   IF    INT
	    #    (      )      [      ,      ;      {      }      =    ELSE  WHILE   VOID
