def pigen():
	value = 4
	denominator = 3
	sign = -1

	yield value

	while(True):
		value  += 4/denominator * sign
		denominator += 2
		sign *= -1 
		yield value

