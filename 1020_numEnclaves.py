def numEnclaves(A):
	## time O(m*n)
	# space O(m * n)
	def dfs(i, j):
		## set cur to 0
		A[i][j] = 0
		for x, y in [(i-1,j),(i+1,j),(i,j-1),(i, j+1)]:
			if 0<= x < m and 0<= y< n and A[x][y]:
				dfs(x, y)

	m, n = len(A), len(A[0])
	for i in range(m):
		for j in range(n):
			if A[i][j] == 1 and (i==0 or i == m-1 or j==0 or j==n-1):
				dfs(i, j)
	return sum(sum(row) for row in A)

print(numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))
print(numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]))