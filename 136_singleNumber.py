def singleNumber(nums):
	# result = [nums.count(ele) for ele in nums]
	# return nums[result.index(1)]
	# for ele in nums:
	# 	if nums.count(ele) ==1:
	# 		return ele
	result =  0
	for ele in nums:
		result ^= ele

	return result

nums = [4,1,2,1,2, 7]
print(singleNumber(nums))