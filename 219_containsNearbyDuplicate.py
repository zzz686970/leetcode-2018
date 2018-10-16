def containsNearbyDuplicate(nums, k):
	## can't ac
	# index = 0
	# for i in range(len(nums)):
	# 	index = nums[i]
	# 	if index in nums[i+1:i+k+1]:
	# 		return True

	# return False
	result = dict()
	for index, value in enumerate(nums):
		if value in result and index - result[value] <= k:
			return True
		result[value] = index
	return False

nums = [1,2,3,2,1, 3, 1]
k = 1
print(containsNearbyDuplicate(nums, k))
