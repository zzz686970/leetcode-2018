# -*- coding: utf-8 -*-
# @Author: zzz686970
# @Date:   2019-02-25 23:24:41
# @Last Modified by:   zzz686970
# @Last Modified time: 2019-02-25 23:43:44

def binary_array_find(arr, target):
	## 左下往上 O(nlogn)
	row, col = 0, len(arr[0]) - 1
	while row < len(arr) and col >= 0:
		if arr[row][col] == target:
			return True
		elif arr[row][col] < target:
			row += 1
		## 右移
		else:
			col -= 1
	return False


def binary_array_find(arr, target):
	## 左下 右上 分开 行列分别进行二分查找
	m, n = len(arr), len(arr[0])
	if arr[0][0] > target or arr[-1][-1] < target:
		return False 

	binary_search_2d(arr, target, 0, m, 0, n)

def binary_search_2d(arr, target, start_x, end_x, start_y, end_y):
	if start_x > end_x or start_y > end_y:
		return False

	x = (start_x + end_x) // 2
	result = binary_search(arr[x], target, start_y, end_y)
	if arr[x][result] == target:
		return True 

	return binary_search_2d(arr, target, start_x, x -1, result +1, end_y) or binary_search_2d(arr, target, x+1, end_x, end_y, result)

def binary_search(arr, target, start, end):
	mid = (start + end) // 2
	if arr[mid] == target:
		return mid 
	elif arr[mid] < target:
		# start = mid +1
		return binary_search(arr, target, mid+1, end)
	else:
		# end = mid 
		return binary_search(arr, target, start, mid-1)

arr = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]

print(binary_array_find(arr, target = 10))