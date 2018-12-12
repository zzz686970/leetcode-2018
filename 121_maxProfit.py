def maxProfit(prices):
	minP, maxP = 0, 0
	result = 
	for i in range(len(prices)):
		if prices[i] < minP:
			minP = prices[i]
			

print(maxProfit([7,1,5,3,6,4]))