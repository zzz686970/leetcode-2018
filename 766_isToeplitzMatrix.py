def isToeplitzMatrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if i+1 < len(matrix) and j+1 < len(matrix[0]) and matrix[i][j] != matrix[i+1][j+1]:
				return False

	return True

matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
matrix1 = [[1,2],[2,2]]
print(isToeplitzMatrix(matrix1))
