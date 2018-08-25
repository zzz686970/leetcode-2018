def maxAreaOfIsland(grid):
	l, w = len(grid), len(grid[0])

	def dfs(i, j):
		if 0<= i < l and 0 <= j < w and grid[i][j]:
			grid[i][j] = 0
			return 1 + dfs(i-1, j) + dfs(i, j+1) + dfs(i+1, j) +  dfs(i, j-1)
		return 0

	area = [dfs(i, j) for i in range(l) for j in range(w) if grid[i][j]]
	return max(area) if area else 0


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(maxAreaOfIsland(grid))
