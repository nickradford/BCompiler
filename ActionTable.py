from BParser import *

cono[11][11] =  {
    #           ** N E X T   O P **
    #                                                        IF    INT
    #   (     )     [     ,     ;     {     }     =   ELSE  WHILE  VOID
    {_xx(),_NO(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx()}, # (         C
    {_xx(),_xx(),_xx(),_xx(),_NO(),_NO(),_xx(),_xx(),_xx(),_xx(),_xx()}, # )         U
    {_xx(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx()}, # [         R
    {_xx(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx()}, # ,         R
    {_CA(),_xx(),_AS(),_xx(),_xx(),_xx(),_EB(),_AS(),_xx(),_NO(),_NO()}, # ;         E
    {_CA(),_xx(),_AS(),_xx(),_xx(),_xx(),_xx(),_AS(),_xx(),_NO(),_NO()}, # {         N
    {_CA(),_xx(),_AS(),_xx(),_xx(),_xx(),_EB(),_AS(),_NO(),_NO(),_NO()}, # }         T
    {_xx(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx()}, # =
    {_xx(),_xx(),_xx(),_xx(),_xx(),_NO(),_xx(),_xx(),_xx(),_xx(),_xx()}, # ELSE      O
    {_CO(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx(),_xx()}, # IF,WHILE  P
    {_DF(),_xx(),_DE(),_DE(),_DE(),_xx(),_xx(),_DE(),_xx(),_xx(),_xx()}  # INT,VOID
  	#                                                        IF    INT
    #   (     )     [     ,     ;     {     }     =   ELSE  WHILE  VOID
}