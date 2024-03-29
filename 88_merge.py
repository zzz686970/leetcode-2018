def merge(nums1, m, nums2, n):
	# while m > 0 and n > 0:
	# 	## compare the last element, put the largest one at end
	# 	if nums1[m-1] >= nums2[n-1]:
	# 		nums1[m+n-1] = nums1[m-1]
	# 		m -= 1 
	# 	else:
	# 		nums1[m+n-1] = nums2[n-1]
	# 		n -= 1
	# if n > 0:
	# 	## if n still remains, then the small numbers should be in the front 
	# 	nums1[:n] = nums2[:n]

	i, j = 0, 0
	while n >0 and m > 0:
		if nums2[n-1] < nums1[m-1]:
			nums1[m+n-1] = nums1[m-1]
			m -= 1
		else:
			nums1[m+n-1] = nums2[n-1]
			n -= 1
	if n:
		nums1[:n] = nums2[:n]


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    for i in range(n):
        bisect.insort_left(nums1, nums2[i], 0, m)
        m += 1
        
    del nums1[m:]

a = [1,2,3,0,0,0]

b = [4,5,6]

merge(a,3, b, 3)
print(a)