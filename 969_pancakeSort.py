def pancakeSort(A):
	## find index 
	moves = []
	for x in range(len(A),1, -1):
		i = A.index(x)
		moves.extend([i+1, x])
		A = A[:i:-1] + A[:i]

	return moves 
