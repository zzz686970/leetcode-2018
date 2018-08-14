def maxSubArray(nums):
	newsum=nums[0]
	max_out=nums[0]
	for i in range(1,len(nums)):
		newsum = max(newsum+nums[i], nums[i])
		max_out = max(newsum, max_out)
		# print(i, newsum, max_out)

	return max_out

nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))