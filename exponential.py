import sys
import matplotlib.pyplot as plt
import math
import numpy

# amount of random numbers to generate
n = 100000
# exponential rate
rate = 1

uDistr = numpy.random.uniform(low=0.0, high=1.0, size=n)

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
