def pancakeSort(A):
	## find index of the next maximum number
	## reverse i+1 numbbers, x will be A[0], insert this to moves
	## reverse x numbers, so x will be A[x-1]
	## repeat N times
	## if permutation is not [1,2,..., A.length], then sorted first 
	moves = []
	# for x in range(len(A),1, -1):
	for x in sorted(A)[::-1]:
		# i = A.index(x)
		moves.extend([idx+1, x])

		## reverse idx..n numbers, 
		A = A[:idx:-1] + A[:idx]

	return moves 
