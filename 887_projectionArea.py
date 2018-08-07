def projectionArea(grid):
	x, y, z = 0, 0, 0
	z = len([y for x in grid for y in x if y>0])
	x = sum([max(x) for x in grid])
	temp = [[0 for i in j] for j in grid]
	for j in range(len(grid[0])):
		for i in range(len(grid)):
			temp[i][j] = grid[j][i]
	y = sum(max(y) for y in temp)

	return x+y+z


grid = [[1,1,1],[1,0,1],[1,1,1]]

print(projectionArea(grid))