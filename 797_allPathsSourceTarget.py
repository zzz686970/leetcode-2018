def allPathsSourceTarget(graph):
	result = []
	for i in graph:
		i.sort()
	path = [0]
	def dfs(n, path):
		for i in graph[n]:
			# print("-----")
			# print(i, path)
			# print("*******")
			path.append(i)
			if i == len(graph) - 1:
				result.append(path[:])
				path.pop()
				if i == graph[n][-1]:
					path.pop()
					# print(path)
				return

			else:
				dfs(i, path)
				if i == graph[n][-1]:
					path.pop()
					# print("^^^^^^^")
					# print(path)
					# print("&&&&&&&&&")
	dfs(0, path)

	return result

graph = [[2,1], [3], [3], []] 
print(allPathsSourceTarget(graph))

