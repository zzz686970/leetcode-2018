def maxDepth(root):
	"""
	:type root: TreeNode
	:rtype: int
	"""

	## DFS
	if not root: return 0
	return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


	## BFS
	stack = [root] if root else []
	level = 0
	while stack:
		queue = []
		for node in stack:
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		stack = queue 
		level += 1

	return level