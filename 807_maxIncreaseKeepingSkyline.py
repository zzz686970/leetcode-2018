def maxIncreaseKeepingSkyline(grid):
	top_bottom_view = []
	left_right_view = []
	total = 0
	gridNew  = [[i for i in row] for row in grid]
	for rows in grid:
		max_row = rows[0]
		for j in rows:
			if j > max_row:
				max_row = j
		left_right_view.append(max_row)

	for i in range(len(grid[0])):
		max_col = grid[0][i]
		for j in range(len(grid)):
			if max_col < grid[j][i]:
				max_col = grid[j][i]
		top_bottom_view.append(max_col)

	for i in range(len(gridNew)):
		for j in range(len(gridNew[0])):
			total += min(top_bottom_view[j], left_right_view[i]) - grid[i][j]
			gridNew[i][j] = min(top_bottom_view[j], left_right_view[i])

	return total


grid = [ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]
print(maxIncreaseKeepingSkyline(grid))