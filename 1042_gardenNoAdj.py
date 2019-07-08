def gardenNoAdj(N: int, paths):
	## initial the list
	ans = [0] * N
	## append each garden with available path
	pool = [[] for _ in range(N)]
	for x, y in paths:
		pool[x-1].append(y-1)
		pool[y-1].append(x-1)

	## for each garden, just pop out one flower based on its paths
	for i in range(N):
		ans[i] = ({1,2,3,4} - {ans[j] for j in pool[i]}).pop()

	return ans

print(gardenNoAdj(N = 4, paths = [[1,2],[3,4]]))