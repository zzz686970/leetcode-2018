def hammingDistance(x, y):
	if len(str('{0:032b}'.format(x))) != len(str('{0:032b}'.format(y))):
		raise ValueError("unequal length")
	return sum(el1 != el2 for el1 , el2 in zip(str('{0:032b}').format(x), str('{0:032b}').format(y)))


x = 1
y = 4
print(hammingDistance(x, y))