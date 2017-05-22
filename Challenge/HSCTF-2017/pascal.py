import math

N = 10**9 + 7

# f = nCk
def f(n, k):
	if k > n:
		return 0
	return math.factorial(n) / math.factorial(n-k) / math.factorial(k)


def matth(n, p):
	s = 0
	k_max = min(n-p, 2*p)
	for k in xrange(k_max+1):
		s += f(n, p+k) * f(2*p, k)
	return s % N


print matth(50, 30), matth(4234, 4000), matth(3000, 1234), matth(2017, 34), matth(4000, 3000), matth(5000, 3000)

# 963267236 350399819 672805854 430233223 155349879 92823536