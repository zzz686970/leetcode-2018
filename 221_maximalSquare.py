def maximalSquare(matrix):
	if not matrix: return 0
	
	m, n = len(matrix), len(matrix[0])
	dp = [[0] for _ in range(len(n)) for _ in range(m)]
	area = 0
	for i in range(m):
		for j in range(n):
			if i == 0 or j == 0:
				dp[i][j] = int(matrix[i][j])
			elif int(matrix[i][j]) == 1:
				dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1

			area = max(area, dp[i][j])

	return area ** 2


