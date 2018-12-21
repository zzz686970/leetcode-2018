def maxProfit(prices):
	# max_val, min_val = 0, 2 ** 31 - 1
	# for i in range(1, len(prices)):
	# 	if prices[i] < min_val: min_val = prices[i]
	# 	elif prices[i] > min_val: max_val = max(prices[i]-min_val, max_val)
	
	# return max_val

	## way2
	if not prices: return 0
	min_val = prices[0]
	dp = [0] * len(prices)
	for i in range(len(prices)):
		dp[i] = max(dp[i-1], prices[i] - min_val)
		min_val = min(prices[i], min_val)
	return dp[-1]

print(maxProfit([7,1,5,3,6,4]))