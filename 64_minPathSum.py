def minPathSum(grid):
	m, n = len(grid), len(grid[0])
	if m < 2 or n < 2: return sum([sum(i) for i in grid])
	# for i in range(1, m):
	# 	grid[i][0] += grid[i-1][0]
	# for i in range(1, n):
	# 	grid[0][i] += grid[0][i-1]

	for i in range(1, m):
		grid[i][0] += grid[i-1][0]
		for j in range(1, n):
			grid[0][j] += grid[0][j-1]
			grid[i][j] += grid[i-1][j] if grid[i-1][j] < grid[i][j-1] else grid[i][j-1]

	return grid[-1][-1]

print(minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))