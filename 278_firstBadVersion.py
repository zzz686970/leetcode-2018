def firstBadVersion(n):
	## can't ac
	# for i in range(n, 0, -1):
	#     if i > 1 and isBadVersion(i):
	#         continue
	#     elif i == 1 and isBadVersion(i):
	#         return i
	#     else:
	#         return i+1

	## can't ac
	# l = 0
	# r = n
	# while l <= r:
	# 	mid = int((l + r-1) /2 )
	# 	if isBadVersion(mid):
	# 		r = mid - 1
	# 	else:
	# 		l = mid + 1

	# return l

	start = 1
	end = n

	while start + 1 < end:
		mid = start + (end - start) / 2
		if isBadVersion(mid):
			end = mid
		else:
			start = mid

	if isBadVersion(start):
		return start
	return end