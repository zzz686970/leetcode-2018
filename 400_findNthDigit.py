def findNthDigit(n):
	## can't ac
	return int("".join(str(char) for char in list(range(1, n+1)))[n-1])
	

print(findNthDigit(3))