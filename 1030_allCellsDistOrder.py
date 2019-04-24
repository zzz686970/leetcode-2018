def allCellsDistOrder(R, C, r0, c0):
	## way1
	result = [[r, c] for r in range(R) for c in range(C)]
	result.sort(key = lambda x: abs(x[0]-r0)+abs(x[1]-c0))
	return result 
	
	# ans = []
	# direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
	# for (x,y )in direction:
	# 	if  0<= r0+x < R and 0<= c0 + y < C:
