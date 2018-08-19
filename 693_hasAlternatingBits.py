def hasAlternatingBits(n):
	binary = bin(n)[2:]
	if '11' in binary or '00' in binary:
		return False

	return True


n = 10
print(hasAlternatingBits(n))