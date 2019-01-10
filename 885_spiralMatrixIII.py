def spiralMatrixIII(self, R, C, r, c):
	"""
	:type R: int
	:type C: int
	:type r0: int
	:type c0: int
	:rtype: List[List[int]]
	"""
	## init list
	res = [[r, c]]
	## x: row	y: col 	n: sequence of index i: step
	x, y, n, i = 0, 1, 0, 0
	while len(res) < R * C:
		## 1 2 2 3 3 3 4 4 4 4...
		r, c, i = r+x, c+y, i +1
		## barrier
		if 0<= r < R and 0<= c < C:
			res.append([r, c])

		## turn right, step changes to default
		## direction (0,1) (1, 0) (0, -1) (-1, 0)
		if i == n//2+1:
			x, y, n, i = y, -x, n+1, 0

	return res
