def addBinary(a, b):
	a = int(a, 2)
	b = int(b,2)

	return str("{0:b}".format((a+b)))

print(addBinary("11", '1'))