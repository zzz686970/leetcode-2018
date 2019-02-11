def kClosest(points, K):
	# res = {}
	# min_num = float('inf')
	# for point in points:
	# 	res[point] = point[0]**point[0] + point[1] * point[1] 

	return heapq.nsmallest(K, points, lambda x: x[0] * x[0] + x[1] * x[1])


