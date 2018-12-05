def surfaceArea(grid):
	## dirty code
	# top = sum([1 for sub in grid for el in sub if el])
	# left_right = []
	# befor_after = []
	# middle = 0
	# for i in range(len(grid)):
	# 	left_right.append(max(grid[i]))
	# temp =  0
	# for i in range(len(grid[0])):
	# 	for j in range(len(grid)):
	# 		if  grid[j][i] > temp:
	# 			temp = grid[j][i]
	# 		if grid[i][j] == 0:
	# 			try:
	# 				if grid[i][j+1]:
	# 					middle += 1
	# 				if grid[i][j-1]:
	# 					middle += 1
	# 				if grid[i-1][j]:
	# 					middle += 1
	# 				if grid[i+1][j]:
	# 					middle += 1
	# 			except:
	# 				pass
	# 	befor_after.append(temp)
	
	# return sum(left_right+befor_after) * 2 + top * 2 + middle

	ans = 0
	for i in range(len(grid)):
		for j in range(len(grid)):
			if grid[i][j]:
				ans += 2 + grid[i][j] * 4
			if i:
				ans -= min(grid[i][j],grid[i-1][j]) * 2
			if j:
				ans -= min(grid[i][j], grid[i][j-1]) * 2

	return ans

grid1= [[1,1,1],[1,0,1],[1,1,1]]
grid = [[1,0],[0,2]]
print(surfaceArea(grid))