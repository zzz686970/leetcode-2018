def kClosest(self, points, K):
	"""
	:type points: List[List[int]]
	:type K: int
	:rtype: List[List[int]]
	"""
	## way 1
	return sorted(points, key=lambda x: x[0]**2+x[1]**2)[:K]

	## way2
	import heapq
	return heapq.nsmallest(K, points, lambda x:x[0]**2+x[1]**2 )