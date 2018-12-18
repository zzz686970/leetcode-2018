def guessNumber(n):
	## time limit
	# while True:
	# 	if guess(n) == 0:
	# 		return n 
	# 	elif guess(n) == -1:
	# 		n += 1
	# 	else:
	# 		n -= 1
	l, r = 1, n 

	## way1
	# while True:
	# 	mid = (l+r) // 2
	# 	if guess(mid) == -1:
	# 		r = mid - 1
	# 	elif guess(mid) == 1:
	# 		l = mid + 1
	# 	else:
	# 		return mid

	## way2
	while l < r:
		mid = (l+r) // 2
		if guess(mid) == 1:
			l = mid + 1
		else:
			r = mid - 1
	return l

