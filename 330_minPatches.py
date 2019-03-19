def minPatches(nums, n):
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