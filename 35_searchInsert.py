def searchInsert(nums, target):
	i = 0
	while i < len(nums):
		if target <= nums[i]:
			return i 
		else:
			i += 1
	return i 

	## way 2
	# return len([x for x in nums if x<target])

assert 2 == searchInsert([1,3,5,6], 5)
assert 1 == searchInsert([1,3,5,6], 2)
assert 4 == searchInsert([1,3,5,6], 7)
assert 0 == searchInsert([1,3,5,6], 0)
