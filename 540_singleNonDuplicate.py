def singleNonDuplicate(nums):
	## O(n)
	# total = sum(nums)
	# repeated = total - sum(set(nums))
	# return total - repeated * 2

	## O(logn)
	l, r = 0, len(nums)-1
	while l < r:
		l, r = 0, len(nums)-1
		while l < r:
			mid = (l+r) // 2
			if mid %2 == 0:
				## unique at right
				if nums[mid] == nums[mid+1]:
					l = mid + 2
				else:
					r = mid
			else:
				## unique part at right
				if nums[mid] == nums[mid-1]:
					l = mid + 1
				else:
					r = mid-1

		return nums[l]

assert 2 == singleNonDuplicate([1,1,2,3,3,4,4,8,8])
assert 10 == singleNonDuplicate([3,3,7,7,10,11,11])