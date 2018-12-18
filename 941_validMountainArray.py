def validMountainArray(A):
	# if len(A) < 3 or A == list(sorted(set(A))) or A[::-1] == list(sorted(set(A))):
	# 	return False

	# idx = A.index(max(A)) + 1
	# return A[:idx] == list(sorted(set(A[:idx]))) and A[idx-1:][::-1] == list(sorted(set(A[idx-1:])))

	## way2
	i, j, n = 0, len(A)-1, len(A)
	while i+1 < n and A[i] < A[i+1]: i += 1
	while j > 0 and A[j-1] > A[j]: j -= 1
	return 0 < i == j < n-1

assert True == validMountainArray([0,3,2,1])