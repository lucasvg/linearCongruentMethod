import sys

# parameters of linear congruent method
a = int(sys.argv[1])
m = int(sys.argv[2])
c = int(sys.argv[3])
x0 = int(sys.argv[4])

##### generates random numbers
curX = x0
for i in xrange(1,10):
	curX = (a*curX + c) % m
	print curX

##### ends generating random numbers