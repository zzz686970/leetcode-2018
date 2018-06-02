def findComplement(num):
	result = "".join(["1" if char=='0' else "0" for char in str('{0:b}'.format(num))])
	return int(result, 2)

print(findComplement(5))
