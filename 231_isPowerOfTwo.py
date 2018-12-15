def isPowerOfTwo(n):
	if not n: return False	
	while n:
		if n == 1: return True
		elif n % 2 ==0:
			n //= 2
		else:
			return False
	return True

assert True == isPowerOfTwo(16)