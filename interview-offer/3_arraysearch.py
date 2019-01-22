def array_search(arr, target):
	if not arr: return False 
	m, n = len(arr), len(arr[0])

	i,j  = n -1 , 0
	while i >=0 and j < m:
		if arr[j][i] > target:
			i -= 1
		elif arr[j][i] < target:
			j += 1

		else:
			return True 

	return False 