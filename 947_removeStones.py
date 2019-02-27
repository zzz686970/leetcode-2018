def removeStones(stones):
	import collections
	def dfs(i, j):
		point.discard((i,j))
		for y in row[i]:
			if (i, y) in point:
				dfs(i, y)

		for x in col[j]:
			if (x, j) in point:
				dfs(x, j)

	point, island, row, col = {(i,j) for (i, j) in stones}, 0, collections.defaultdict(list), collections.defaultdict(list)
	for i, j in stones:
		row[i].append(j)
		col[j].append(i)
	for i, j in stones:
		if (i, j) in point:
			dfs(i, j)
			island += 1

	return len(stones) - island

print(removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))


### union find
def removeStones(stones):
	"""[summary]
	
	{0: -1, -1: -1}
	{0: -1, -1: -2, -2: -2}
	{0: -1, -1: -2, -2: -2, 1: -2}
	{0: -1, -1: -2, -2: -3, 1: -2, -3: -3}
	{0: -1, -1: -2, -2: -3, 1: -2, -3: -3, 2: -3}
	{0: -1, -1: -2, -2: -3, 1: -2, -3: -3, 2: -3}
	[-3, -3, -3, -3, -3, -3]
	
	Arguments:
		stones {[type]} -- [description]
	
	Returns:
		[type] -- [description]
	"""	
	island = {}

	def find(x):
		if x != island[x]:
			island[x] = find(island[x])

		return island[x]

	def union(x, y):
		island.setdefault(x, x)
		island.setdefault(y, y)
		# island[x] = x 
		# island[y] = y 
		island[find(x)] = find(y)
		print(island)


	for i, j in stones:
		union(i, ~j)
	print([find(x) for x in island])
	return len(stones) - len({find(x) for x in island})

print(removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
