def intersection(nums1, nums2):
	# return list(set([i for i in nums1 if i in nums2]))
	return list(set(nums1).intersection(nums2))

print(intersection([1,2,2,1,],[2,2]))