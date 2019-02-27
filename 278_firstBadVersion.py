def firstBadVersion(n):
	## can't ac
	# for i in range(n, 0, -1):
	#     if i > 1 and isBadVersion(i):
	#         continue
	#     elif i == 1 and isBadVersion(i):
	#         return i
	#     else:
	#         return i+1

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


def firstBadVersion(n):
	l, r = 0, n
	while l < r:
		mid = (l + r) // 2
		if isBadVersion(mid):
			r = mid
		else:
			l = mid + 1

	return l
