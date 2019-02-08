def maxChunksToSorted(arr):
	## for each block [i,j] should include i~j, len = j-1 + 1
	"""
	The basic idea is to use max[] array to keep track of the max value until the current position,
	compare it to the sorted array (indexes from 0 to arr.length - 1). 
	If the max[i] equals the element at index i in the sorted array, then the final count++.
	""" 
	if not arr: return 0
	cnt = 0
	max_val = 0
	for i in range(len(arr)):
		max_val = max(max_val, arr[i])
		if max_val == i:
			cnt += 1

	return cnt 

print(maxChunksToSorted(arr = [4,3,2,1,0]))
