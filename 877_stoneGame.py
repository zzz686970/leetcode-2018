def stoneGame(piles):
	## way 1 
	## hint: always pick odd or even piles
	# return True 

	## way 2 dp 2d
	l = len(piles)
	dp = [[0]* l for _ in range(l)]
	for i in range(l): dp[i][i] = piles[i]

	for d in range(1, l):
		for i in range(l-d):
			dp[i][i+d] = max(piles[i]-dp[i+1][i+d], piles[i+d]-dp[i][i+d-1])

	return dp[0][-1]> 0


	## way 3

	l = len(piles)
	dp = piles[:]
	for d in range(1, l):
		for i in range(l-d):
			dp[i] = max(piles[i]-dp[i+1], piles[i+d]-dp[i])
	return dp[0] > 0

