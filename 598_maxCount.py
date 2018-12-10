def maxCount(m, n, ops):
	maxCount = 1
	if not ops: return m*n

	for el in list(zip(*ops)):
		maxCount *= min(el)
	return maxCount

	# array = [[0 for _ in range(n)] for _ in range(m)]

	# for el in ops:
	# 	a, b = el[0], el[1]
	# 	for i in range(len(array)):
	# 		for j in range(len(array[0])):
	# 			if i < a and j < b:
	# 				array[i][j] += 1

	# return array

# array 
# print(maxCount(m=3, n=3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]))
print(maxCount(m=3, n=3, ops= []))