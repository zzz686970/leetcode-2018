def search(nums, target):
	l, h = 0, len(nums)
	while l < h:
		mid = (l+h) // 2
		if (nums[mid] < nums[0]) == (target < nums[0]):
			if nums[mid] < target:
				l = mid + 1
			elif nums[mid] > target:
				h = mid 
			else:
				return mid 

		elif target < nums[0]:
			l = mid + 1
		else:
			h = mid 

	return -1