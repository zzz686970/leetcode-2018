def intersect(nums1, nums2):
	import collections
	a1 = collections.Counter(nums1)
	a2 = collections.Counter(nums2)
	print(a1)
	result = []
	for a in a1:
		if a in a2:
			c = min(a1[a], a2[a])
			for i in range(c):
				result.append(a)

	return result

print(intersect(nums1=[1,2,2,1], nums2=[2,2]))