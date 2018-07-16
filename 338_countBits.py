def countBits(num):
	result = []
	for i in range(num+1):
		x = str('{0:b}').format(i)
		result.append( sum([int(char) for char in str('{0:b}').format(i)]))
	return result


print(countBits(5))