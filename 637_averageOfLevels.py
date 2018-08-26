import collections
def averageOfLevels(root):
	## way 1
	# result = {}
	# result.setdefault(depth, []).append(node.val)
	result = collections.defaultdict(list)

	def dfs(node, depth):
		if node:
			result[depth].append(node.val)
			dfs(node.left, depth+1)
			dfs(node.right, depth + 1)

	dfs(root, 0)
	return list(map(lambda x: sum(x)/len(x), result.values()))

	## way 2
	# result, level = [], [root]
	# while result and level:
	# 	result.append([node.val for node in level])
	# 	level = [child for node in level for child in (node.left, node.right) if child]

	# avg = [sum(result[i]/len(result[i])) for i in range(len(result))]
	# return avg

