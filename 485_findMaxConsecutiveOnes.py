def findMaxConsecutiveOnes(nums):
	result = []
	index = 0
	for i in range(len(nums)):
		if nums[i] == 1:
			index += 1
		else:
			result.append(index)
			index = 0

	result.append(index)

	return max(result)

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
