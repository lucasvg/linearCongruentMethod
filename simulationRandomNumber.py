import sys

#### load parameters of Linear Congruent method
# a of L. C. formula
a = int(sys.argv[1])
# M of L. C. formula
m = int(sys.argv[2])
# c of L. C. formula
c = int(sys.argv[3])
# seed of L. C. formula
x0 = int(sys.argv[4])
# amount of random numbers to generate
n = int(sys.argv[5])
#### end load parameters of linear congruent method

numbers = []
##### generates random numbers
curX = x0
for i in xrange(0,n):
	curX = (a*curX + c) % m
	numbers.append(curX)
##### ends generating random numbers

print numbers