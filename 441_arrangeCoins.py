def arrangeCoins(n):
	return int((2*n+0.25)**0.5-0.5)

	## way2 
	# k = 1
	# while n >= 0:
	# 	n -= k
	# 	k += 1
	# return k-2

print(arrangeCoins(5))