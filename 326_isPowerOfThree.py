def isPowerOfThree(n):
	if not n: return False	
	while n:
		if n == 1: return True
		elif n % 3 ==0:
			n //= 3
		else:
			return False
	return True

assert True == isPowerOfThree(27)