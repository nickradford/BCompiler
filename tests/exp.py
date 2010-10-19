import sys
sys.path.append("../")

from ExpressionParser import *

exp = ExpressionParser()

print exp

exp.testExpression("test.txt")