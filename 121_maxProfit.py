def maxProfit(prices):
	max_val, min_val = 0, 2 ** 31 - 1
	for i in range(1, len(prices)):
		if prices[i] < min_val: min_val = prices[i]
		elif prices[i] > min_val: max_val = max(prices[i]-min_val, max_val)
	
	return max_val


print(maxProfit([7,1,5,3,6,4]))