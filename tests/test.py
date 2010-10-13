import sys
sys.path.append("../")
from Compiler import *

list = [123, 234, 345, 456, 567, 678, 789 ,890]

for num in list:
	print Compiler.long2string(num)