def getSum(a, b):
	## way1
	# return sum([a,b])

	## way2
	## reference https://leetcode.com/problems/sum-of-two-integers/discuss/132479/Simple-explanation-on-how-to-arrive-at-the-solution/168383
	while  b != 0:
		carry = a & b
		a = (a ^ b) % 0x100000000
		b = (carry << 1) % 0x100000000

	return a if a <= 0x7FFFFFFF else a | (~0x100000000+1)