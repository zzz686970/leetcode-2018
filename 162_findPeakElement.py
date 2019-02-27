"""1D version

	## compare the element left or right of mid with the mid element

Variables:
	print(findPeakElement([1,2,3,1])) {[type]} -- [description]
	print(findPeakElement([1,2,1,3,5,6,4])) {[type]} -- [description]
"""

def findPeakElement(nums):
	## compare the element left or right of mid with the mid element
	l, r = 0, len(nums) -1 
	while l < r:
		mid = (l + r) // 2
		if nums[mid] < nums[mid+1]:
			l = mid + 1
		else:
			r = mid 

	return l

"""2D

pick col j = m // 2 
find the global max of the col i, j
compare (i, j) with (i, j-1) and (i, j+1)
if (i, j) >= (i,j-1) and (i, j + 1), found 2D peak
"""

print(findPeakElement([1,2,3,1]))
print(findPeakElement([1,2,1,3,5,6,4]))