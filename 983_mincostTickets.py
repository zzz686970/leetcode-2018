def mincostTickets(days, costs):
	dp = [0 for _ in range(days[-1]+1)]
	for i in range(days[-1]+1):
		if i not in days:
			dp[i] = dp[i-1]
		else:
			dp[i] = min(dp[max(i-1, 0)]+costs[0], dp[max(i-7, 0)]+costs[1], dp[max(i-30, 0)]+costs[2])

	return dp[-1]

print(mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))