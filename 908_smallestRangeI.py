def smallestRangeI(A, K):
	temp = sorted(A)
	small = temp[0]
	large = temp[-1]
	return large-small - 2*K if large-small - 2*K > 0 else 0

A = [0, 10]
K = 2
print(smallestRangeI(A, K))