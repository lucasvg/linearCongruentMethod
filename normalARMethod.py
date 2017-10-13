import sys
import matplotlib.pyplot as plt
import math
import numpy

# amount of tries to generate
n = 100000
# exponential rate
rate = 1

def accept(u, y):
	return u <= math.pow(math.e, -((y-1)**2)/2)

# computes normal
normalDistrNumbers = []
for i in range(0, n):
	uDistr = numpy.random.uniform(low=0.0, high=1.0, size=2)
	uForExp = numpy.random.uniform(low=0.0, high=1.0, size=1)[0]
	exp = ( (-1/rate) * math.log(uForExp) )

	if(accept(uDistr[0], exp)):
		if (uDistr[1] > 0.5):
			normalDistrNumbers.append(exp)
		else:
			normalDistrNumbers.append(-exp)
# ends computing normal

data = normalDistrNumbers
plt.hist(data, bins=50, weights=numpy.zeros_like(data) + 1. / len(data))
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
