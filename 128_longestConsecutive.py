def longestConsecutive(nums):
	init = {x: False for x in nums}
	result = 0
	for i in nums:
		if init[i] is False:
			init[i] = True
			left, right = init.get(i-1, 0), init.get(i+1, 0)
			length = 1+ left + right
			result, init[i-left], init[i+right] = max(result, length), length, length

	return result

nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))