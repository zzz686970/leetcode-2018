def findMaxLength(nums):
	d = {0: 0}
	key = 0
	max_l = 0
	for i in range(len(nums)):
		key += nums[i] or -1
		if key not in d:
			d[key] = i + 1
		else:
			max_l = max(max_l, i+1 - d[key])

	return max_l


print(findMaxLength([1,0,0,1,1,1]))