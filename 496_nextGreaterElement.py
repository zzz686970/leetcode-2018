def nextGreaterElement(nums1, nums2):
	# nums1 = sorted(nums1)
	# nums2 = sorted(nums2)
	result = []
	for i in range(len(nums1)):
		current = nums2.index(nums1[i])
		if current < len(nums2):
			for j in range(current, len(nums2)):
					if nums2[j] > nums1[i]:
						result.append(nums2[j])
						break
					elif j == len(nums2) -1:
						result.append(-1)
	
	return result

a = [4,1,2]
b = [1,3,4,2]
print(nextGreaterElement(a, b))
