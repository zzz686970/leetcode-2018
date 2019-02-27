def findClosestElements(arr, k, x):
	l, r = 0, len(arr) - k 
	while l < r:
		mid = (l + r) // 2
		## not so close enough, move to the right
		if x - arr[mid] > arr[mid+k] - x:
			l = mid + 1
		else:
			r = mid 

	return arr[l:l+k]

print(findClosestElements([1,2,3,4,5], k=4, x=3))
print(findClosestElements([1,2,3,4,5], k=4, x=-1))