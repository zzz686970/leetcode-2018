def searchMatrix(matrix, target):
	## O(m + n)
	## search from last element of each row
	j = -1
	for row in matrix:
		while j + len(row) >=0 and row[j] > target:
			j -= 1

		if j + len(row) >=0 and  row[j] == target:
			return True 

	return False 