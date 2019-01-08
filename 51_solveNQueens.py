def solveNQueens(n):
	arr = [[0 for _ in range(len(n))] for _ in range(len(n))]

	for i in range(len(arr)):
		for j in range(len(arr[0])):
			