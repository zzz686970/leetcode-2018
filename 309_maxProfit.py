def maxProfit(prices):
	## initial profit during free, have and cool stage
	## free means can purchase another stock, so the last round must be free or cool
	## have means already bought some stocks, so the last round must be free
	## cool means , the last round should be have
	## have and cool, we didn't buy the stock at 0 price, so can't initialize to 0
	free, have, cool = 0, float('-inf'), float('-inf')
	for p in prices:
		## for have, if last round is free, then profit need to adjust because of buying
		## for cool, since last round is have, we need to add the value
		free, have, cool = max(free, cool), max(have, free - p), have + p 

	return max(free, cool)
