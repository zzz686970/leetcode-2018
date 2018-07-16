def allPathsSourceTarget(graph):
	result = []
	def dfs(x, path):
		if x == len(graph) - 1:
			result.append(path)
			for z in graph[x]:
				dfs(z, path+[z])
			dfs(0, [0])

	return result

graph = [[1,2], [3], [3], []] 
print(allPathsSourceTarget(graph))

