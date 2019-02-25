"""[summary]

[given a sorted binary, efficiently find the number of 1's]
arr = [0,0,0,0, 1,1,1,1,1]
""" 

## O(log(n))
# def binary_sorted_array(arr):
# 	n = len(arr)
# 	if arr[-1] == 0:
# 		return 0

# 	if arr[0]:
# 		return n

# 	return binary_sorted_array(arr[:n//2]) + binary_sorted_array(arr[n//2:])

## O(log(n)) non-recursive
def binary_sorted_array(arr):
	l, r = 0, len(arr)-1
	while l <= r:
		mid = (l + r) // 2
		if arr[mid] == 1:
			r = mid -1
		else:
			l = mid + 1
	return len(arr) - l 
	


print(binary_sorted_array([0,0,0,0, 1,1,1,1,1]))