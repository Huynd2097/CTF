import math


def findN(number1,number2):
	for x in xrange(2,500):
		log1 = int(math.log(number1,x))
		log2 = int(math.log(number2,x))

		if log2 > log1:
			return 2**log2
		return 0


print findN(500,600)