def arrangeCoins(n):
	## n(n+1) = 2t --> (n+0.5)^2 = 2t + 0.25
	return int((2*n+0.25)**0.5-0.5)

	## way2 
	# k = 1
	# while n >= 0:
	# 	n -= k
	# 	k += 1
	# return k-2


## binary search
def arrangeCoins(n):

	l, r = 0, n 
	while l < r:
		mid = (l +r) // 2
		if mid * (mid + 1) // 2 < n:
			l = mid + 1
		else:
			r = mid
	print(l, r)
	return l


print(arrangeCoins(7))