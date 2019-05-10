def divisorGame(N):
	## for even numbers, always win
	# for odd numbers, give opponent a chance to win
	return N & 1 == 0