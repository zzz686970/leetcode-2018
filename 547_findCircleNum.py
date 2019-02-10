# import numpy as np 
# def findCircleNum(M: 'List[List[int]]') -> 'int':
# 	print((np.matrix(M, dtype=np.bool)**len(M)).A)
# 	return len(set(map(tuple, (np.matrix(M, dtype=np.bool)**len(M)).A)))


def findCircleNum(M: 'List[List[int]]') -> 'int':
	n = len(M)
	visited = set()
	def dfs(node):
		for i, val in enumerate(M[node]):
			if i and val not in visited:
				visited.add(i)
				dfs(i)

	ans = 0
	for i in range(n):
		if i not in visited:
			dfs(i)
			ans += 1

	return ans 

print(findCircleNum([[1,1,0],
 [1,1,1],
 [0,1,1]]))