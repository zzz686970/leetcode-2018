def countNegatives(grid):
	## O(M*N) ==> O(N^2)
	# return sum([grid[i][j] < 0 for i in range(len(grid)) for j in range(len(grid[0]))])

	## O(m+n)
	

if __name__ == '__main__':
	print(countNegatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
	print(countNegatives(grid = [[3,2],[1,0]]))
	print(countNegatives(grid = [[1,-1],[-1,-1]]))
	print(countNegatives(grid = [[-1]]))