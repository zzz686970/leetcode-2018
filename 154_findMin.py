def findMin(nums):
	## when nums[mid] == nums[r]
	## we are not sure the minimum in mid's left or right, hence upper bound - 1
	l, r= 0, len(nums) - 1
	while l < r:
		mid = (l + r) // 2
		if nums[mid] > nums[r]:
			l = mid + 1
		elif nums[mid] < nums[r]:
			r = mid 
		else:
			r = r - 1
	print(l, r)

	return nums[l]


print(findMin([3,3,1,3]))
