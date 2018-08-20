def maxDepth(root):
	"""
	:type root: TreeNode
	:rtype: int
	"""

	## DFS
	if not root: return 0
	return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

	###   BFS     
	# if root == None:
	# 	return 0

	# 	depth = 0
	# 	q = [root]
	# 	while len(q) != 0:
	# 		depth += 1
	# 		for i in range(0, len(q)):
	# 			if q[0].left:
	# 				q.append(q[0].left)
	# 			if q[0].right:
	# 				q.append(q[0].right)
	# 			del q[0]
	# 	return depth