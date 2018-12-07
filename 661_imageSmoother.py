def imageSmoother(M):
	result = [[0 for i in range(len(M[0]))] for j in range(len(M))]
	direction = [(0,0), (0,1),(0,-1),(1,0),(-1,0),(-1,1),(1,1),(-1,-1),(1,-1)]
	for i in range(len(M)):
		for j in range(len(M[0])):
			total, cnt = 0, 0
			for r, c in direction:
				if i+r < 0 or j+c < 0 or i+r >= len(M) or j+c >= len(M[0]):
					continue
				total += M[i+r][j+c]
				cnt += 1
			result[i][j] = total // cnt

	return result



M = [[1,1,1],
 [1,0,1],
 [1,1,1]]
print(imageSmoother(M))