def minFallingPathSum(A):
	dp = A[0]
	for row in A[1:]:
		dp = [value+min(dp[c], dp[max(c-1,0)], dp[min(len(A)-1, c+1)]) for c, value in enumerate(row)]
	return min(dp)

print(minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))