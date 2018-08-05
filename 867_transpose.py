def transpose(A):
	row = len(A)
	col = len(A[0])
	result = [[] for x in range(col)]
	print(result)
	for i in range(row):
		for j in range(col):
			result[j].append(A[i][j])

	return result

print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
