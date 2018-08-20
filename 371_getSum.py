def getSum(a, b):
	while  b != 0:
		carry = a & b
		a = (a ^ b) % 0x100000000
		b = (carry << 1) % 0x100000000

	return a if a <= 0x7FFFFFFF else a | (~0x100000000+1)