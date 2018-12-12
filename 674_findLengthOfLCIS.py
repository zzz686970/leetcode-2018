def findLengthOfLCIS(nums):
	if len(nums) <= 1: return len(nums)
	slow, fast = 0, 1
	result = []
	while fast <= len(nums)-1:
		if nums[fast] <= nums[fast-1]:
			result.append(fast-slow)
			slow = fast
		fast += 1
	result.append(fast-slow)
	return max(result)

print(findLengthOfLCIS(nums=[1,3,5,4,7]))
