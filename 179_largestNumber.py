def largestNumber(nums):
	nums = [str(x) for x in nums]
	longest = max([len(x) for x in nums], default = 0)
	nums.sort(key=lambda x: x*(longest//len(x) +1), reverse=True)
	if nums and nums[0] == '0':
		return '0'

	return ''.join(nums)

print(largestNumber([3,30,34,5,9]))