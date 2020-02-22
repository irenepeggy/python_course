
def BinPow(a, n, f):
	if (n == 1):
		return a
	elif (n & 1 == 1):
		return f(a, BinPow(a, n-1, f))
	else:
		semipow = BinPow(a, n >> 1, f)
		return f(semipow, semipow)