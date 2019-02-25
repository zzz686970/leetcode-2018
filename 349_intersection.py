def intersection(nums1, nums2):
	# return list(set([i for i in nums1 if i in nums2]))
	return list(set(nums1).intersection(nums2))

print(intersection([1,2,2,1,],[2,2]))


## binary approach
def intersection(nums1, nums2):
	nums1, nums2 = sorted([nums1, nums2], key= len)
	nums1.sort()
	result = set()
	for val in nums2:
		l, r = 0, len(nums1)
		while l < r:
			mid = (l+r) // 2
			if nums1[mid] == val:
				result.add(val)
				break
			elif nums1[mid] < val:
				l = mid
			else:
				r = mid - 1
	return list(result)


print(intersection(nums1 = [1,2,2,1], nums2 = [2,2]))