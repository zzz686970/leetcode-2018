def deckRevealedIncreasing(deck):
	# d = []
	# for x in sorted(deck)[::-1]:
	# 	d = [x] + d[-1:]+d[:-1]
	# return d

	ind = list(range(len(deck)))
	for num in sorted(deck):
		deck[ind[0]] = num 
		ind = ind[2:] + [ind[1]] if len(ind) > 1 else []
	
	return deck
