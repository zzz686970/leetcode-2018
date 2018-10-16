def mySqrt(x):
	# return int(x ** 0.5)

	## binary search
	start = 0
	end = x
	while end > start:
		mid = start + (end-start) // 2
		if mid ** 2 == x: 
			return mid
		elif mid ** 2 > x:
			end = mid - 1
		else:
			if (mid+1) ** 2 > x:
				return mid
			else:
				start = mid + 1
	return start

print(mySqrt(8))