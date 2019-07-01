def duplicateZeros(arr):
	## return 
	idx = 0
	size = len(arr)
	while idx < size:
		if arr[idx] == 0:
			arr = arr[:idx] + [0] + arr[idx:size-1]
			idx += 1
		idx += 1

	return arr 

def duplicateZeros(arr):
	## in-place 
	idx = 0
	size = len(arr)
	while idx < size:
		if arr[idx] == 0:
			arr[idx:] = [0] + arr[idx:size-1]
			idx += 1
		idx += 1

	return arr 

print(duplicateZeros([1,0,2,3,0,4,5,0]))