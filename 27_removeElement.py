def removeElement(nums, val):
	# for i in range(nums.count(val)):
	# 	nums.remove(val)
	# return len(nums)

	start, end = 0, len(nums) -1
	while start <= end:
		if nums[start] == val:
			nums[start], nums[end], end = nums[end], nums[start], end-1
		else:
			start += 1

	return start
