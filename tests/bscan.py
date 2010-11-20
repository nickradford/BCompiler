import sys
sys.path.append("../")

from BScanner import *

print "----------"
print "check/e1.b"
print "----------"
bscan = BScanner("check/e1.b")



try:
	while True:
		x = bscan.nextToken()
		print x.getTokenType(), x.toString()
except:
	x = Token(TokenType.END_FILE, 'EOF')
	print x.getTokenType(), x.toString()
	

print "----------"
print "check/e2.b"
print "----------"
bscan = BScanner("check/e2.b")



try:
	while True:
		x = bscan.nextToken()
		print x.getTokenType(), x.toString()
except:
	pass

print "----------"
print "check/e3.b"
print "----------"
bscan = BScanner("check/e3.b")



try:
	while True:
		x = bscan.nextToken()
		print x.getTokenType(), x.toString()
except:
	pass
	
print "----------"
print "check/t1.b"
print "----------"
bscan = BScanner("check/t1.b")



try:
	while True:
		x = bscan.nextToken()
		print x.getTokenType(), x.toString()
except:
	pass
	
	
print "----------"
print "check/t2.b"
print "----------"
bscan = BScanner("check/t2.b")



try:
	while True:
		x = bscan.nextToken()
		print x.getTokenType(), x.toString()
except:
	pass
	
print "----------"
print "check/t3.b"
print "----------"
bscan = BScanner("check/t3.b")



try:
	while True:
		x = bscan.nextToken()
		print x.getTokenType(), x.toString()
except:
	pass