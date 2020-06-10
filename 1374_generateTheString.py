def generateTheString(n):
	"""
	n & 1 to check whether it's odd or even
	if odd: bbb
	if even: baaa
	"""
	return 'b' + 'ab'[n & 1] * (n - 1)