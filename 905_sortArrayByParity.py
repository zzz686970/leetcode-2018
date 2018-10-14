def sortArrayByParity(A):
	"""
	:type A: List[int]
	:rtype: List[int]
	"""
	B = []
	C = []
	for el in A:
		if el % 2:
			B.append(el)
		else:
			C.append(el)
	return C+B

A = [3,1,2,4]
print(sortArrayByParity(A))

        