def pivotIndex(nums):
	## find index around mid
	# visited, mid = [], len(nums) // 2
	# while mid not in visited and 0<=mid < len(nums):
	# 	if sum(nums[mid+1:]) > sum(nums[:mid]):
	# 		visited.append(mid)
	# 		mid -= 1
	# 	elif sum(nums[mid+1:]) < sum(nums[:mid]):
	# 		visited.append(mid)
	# 		mid += 1
	# 	else:
	# 		return mid
	# return -1

	## time limit
	# for i in range(len(nums)):
	# 	if sum(nums[:i]) == sum(nums[i+1:]):
	# 		return i 

	# return -1
	l, total = 0,  sum(nums)
	for i, num in enumerate(nums):
		if 2 * l == total - num:
			return i 
		l += num 
	return -1

print(pivotIndex(nums=[1,2,0,3]))