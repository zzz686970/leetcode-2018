def findUnsortedSubarray(nums):
	left = 0
	right = len(nums)
	result = sorted(nums)
	for i in range(len(result)):
		if result[i] ==nums[i]:
			left += 1
		else:
			break

	for j in range(len(result)-1, 0, -1):
		if result[j] == nums[j]:
			right -= 1
		else:
			break

	return len(nums[left:right])

nums = [2, 6, 4, 8, 10, 9, 15]
print(findUnsortedSubarray(nums))