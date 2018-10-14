def sortArrayByParityII(A):
	odd = []
	even = []
	result = [0 for i in range(len(A))]
	for el in A:
		if el % 2:
			odd.append(el)
		else:
			even.append(el)
	for i in range(len(even)):
		result[i*2] = even[i]
	for j in range(len(odd)):
		result[j*2+1] = odd[j]

	return result 
	# even = []
	# odd = []
	# odd.append(A[0]) if A[0] % 2 else even.append(A[0])
	# for i in range(1, len(A)):
	# 	if i % 2:
	# 		odd.append(A[i])
	# 	else:
	# 		even.append(A[i])
	# return odd

A = [4,2,5,7]
print(sortArrayByParityII(A))

        