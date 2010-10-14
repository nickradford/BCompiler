import sys
sys.path.append("../")

from BScanner import *

bscan = BScanner("test.txt")



try:
	while True:
		x = bscan.nextToken()
		print x
		print x.toString()
except:
	exit()
