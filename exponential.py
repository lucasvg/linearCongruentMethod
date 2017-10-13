import sys
import matplotlib.pyplot as plt
import math

#### load parameters of Linear Congruent method
# a of L. C. formula
a = 37
# M of L. C. formula
m = 23597
# c of L. C. formula
c = 7
# seed of L. C. formula
x0 = 4
# amount of random numbers to generate
n = 100000
# exponential rate
rate = 1

def genUniform(a, m, c, x0, n):
	uniformDistrNumbers = []
	curX = x0
	for i in xrange(0,n):
		curX = (a*curX + c) % m
		uniformNumber = curX/float(m)
		uniformDistrNumbers.append(uniformNumber)
	return uniformDistrNumbers

uDistr = genUniform(a, m, c, x0, n)
expDistrNumbers = []
for u in uDistr:
	expDistrNumbers.append( (-1/rate) * math.log(u) )

data = expDistrNumbers
binwidth = 1
plt.hist(data, bins=range(int(math.floor(min(data))), int(math.ceil(max(data) + binwidth)), binwidth))
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
