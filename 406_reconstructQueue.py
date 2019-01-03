def reconstructQueue(people):
	## O(n^2)
	res = []
	people = sorted(people, key = lambda x: (-x[0],x[1]))
	for p in people:
		res.insert(p[1],p)
		# print(res)

	return res 

	## O(n sqrt(n))
	


print(reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))