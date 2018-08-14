def longestConsecutive(nums):
	init = {x: False for x in nums}
	result = 1
	for i in nums:
		if init[i] is False:
			init[i] = True
			left, right = init.get(i-1, 0), init.get(i+1, 0)
			length = 1+ left + right
			result, init[i-left], init[i+left] = max(result, length), length, length

	return result

nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))