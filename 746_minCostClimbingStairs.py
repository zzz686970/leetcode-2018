def minCostClimbingStairs(cost):
	dp = [0 for _ in range(len(cost))]
	dp[0], dp[1] = cost[0], cost[1]
	for i in range(2, len(cost)):
		dp[i] = min(dp[i-2]+cost[i],dp[i-1]+cost[i])

	return min(dp[-2], dp[-1])

print(minCostClimbingStairs([10,15,20]))