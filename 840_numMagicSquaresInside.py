def numMagicSquaresInside(grid):
	"""
	:type grid: List[List[int]]
	:rtype: int
	"""
	cnt = 0
	def isMagic(i, j):
		s = "".join(str(grid[i - x // 3][j - x % 3]) for x in [0, 1, 2, 5, 8, 7, 6, 3])
		return [1 if grid[i][j] % 2 == 0 and (s in "27618349" * 2 or s in "27618349"[::-1] * 2) else 0]
	for i in range(2, len(grid)):
		for j in range(2, len(grid[0])):
			if grid[i-1][j-1] == 5:
				cnt += sum(isMagic(i,j))
	return cnt
	# return sum(isMagic(i, j) for i in range(len(grid) - 2) for j in range(len(grid[0]) - 2) if grid[i + 1][j + 1] == 5)

print(numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))