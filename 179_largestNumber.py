def largestNumber(nums):
	nums = [str(x) for x in nums]
	longest = max([len(x) for x in nums], default = 0)

	## 121 12  
	nums.sort(key=lambda x: x*(longest//len(x) +1), reverse=True)
	if nums and nums[0] == '0':
		return '0'

	return ''.join(nums)

	## way2
	# from functools import cmp_to_key
	# def cmp(a, b):
	# 	return int(b+a) - int(a+b)

	# nums = list(map(str, nums))
	# nums.sort(key=cmp_to_key(cmp))
	# return ''.join(nums).lstrip('0') or '0'


print(largestNumber([3,30,34,5,9]))