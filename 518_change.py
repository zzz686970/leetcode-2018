def change(amount, coins):
	## create a list from 0 to amount
	dp = [0] * (amount + 1)
	dp[0] = 1

	## each coin is like a step
	for i in coins:
		for j in range(1, amount+1):
			if j >= i:
				dp[j] += dp[j-i]

	return dp[amount]

print(change(5, [1,2,5]))
