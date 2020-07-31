def minPatches(nums, n):
	"""
	[1,2,4] --> [1, 8) +8 for next round
	[1,2,4,13] --> [1, 29)
	"""
	i , miss, add = 0, 1, 0
	while miss <= n:
		if i < len(nums) and nums[i] <= miss:
			miss += nums[i]
			i += 1
		else:
			miss += miss 
			add += 1

	return add 

print(minPatches(nums = [1, 2, 4, 13, 43], n = 100))