def largestPerimeter(A):
	for num in range(len(sorted(A)[::-1])-2):
		if A[num] < A[num+1] + A[num+2]:
			return A[num] + A[num+1] + A[num+2]

	return 0