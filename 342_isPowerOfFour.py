def isPowerOfFour(num):
	return num != 0 and num &(num-1) == 0 and num & 1431655765== num

assert True == isPowerOfFour(16)
