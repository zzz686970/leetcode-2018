# def pancakeSort(A):
# 	## find index of the next maximum number
# 	## reverse i+1 numbbers, x will be A[0], insert this to moves
# 	## reverse x numbers, so x will be A[x-1]
# 	## repeat N times
# 	## if permutation is not [1,2,..., A.length], then sorted first 
# 	moves = []
# 	# for x in range(len(A),1, -1):
# 	for x in sorted(A)[::-1]:
# 		idx = A.index(x)
# 		# print(x, idx, A)

# 		moves.extend([idx+1, x])

# 		## reverse idx+1...n numbers, 
# 		A = A[:idx:-1] + A[:idx]
# 	return moves 

# print(pancakeSort([4,3,5,7,1]))


def pancakeSort(A):
	l = len(A) 
	moves = []
	while l > 1:
		cur_index = A.index(max(A[:l]))
		A = (A[:cur_index+1][::-1] + A[cur_index+1:l])[::-1] + A[l:]

		moves.extend([cur_index+1, l])
		l -= 1
	print(A)
	return moves

print(pancakeSort([3,2,4, 1, 5,0 ]))

