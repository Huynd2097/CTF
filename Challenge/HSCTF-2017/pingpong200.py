import math
import sys
def fibo(n):
	sqrt5 = math.sqrt(5)
	fn = 1/sqrt5 * ((1+sqrt5) / 2)**n - 1/sqrt5 * ((1-sqrt5) / 2)**n
	return int(round(fn,0))
n = sys.argv(1)
print fibo(n)