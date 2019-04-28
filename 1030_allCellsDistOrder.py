def allCellsDistOrder(R, C, r0, c0):
	## way1
	result = [[r, c] for r in range(R) for c in range(C)]
	result.sort(key = lambda x: abs(x[0]-r0)+abs(x[1]-c0))
	return result 


## dfs
def allCellsDistOrder(R, C, r0, c0):
	## way2
	def dfs(i, j):
		seen.add((i, j))
		res.append([i, j])
		for x,y in ((i-1, j),(i+1, j), (i, j-1),(i, j+1)):
			if 0 <= x < R and 0<= y < C and (x,y) not in seen:
				dfs(x, y)

	res, seen = [], set()
	dfs(r0, c0)
	return sorted(res, key = lambda t: abs(t[0]-r0) + abs(t[1]-c0))


## bfs
def allCellsDistOrder(R, C, r0, c0):
	## way3
	res, seen, bfs = [], {(r0, c0)}, [[r0,c0]]
	while bfs:
		res += bfs 
		new = []
		for i,j in bfs:
			for x, y in ((i-1, j),(i+1, j),(i,j-1),(i, j+1)):
				seen.add((x, y))
				new.append([x, y])

		bfs = new 
	
	return res 
	


