def convertBST(root):
	ans = 0
	stack = []
	stack.append([root, 0])
	while stack:
		node, visited = stack.pop()
		if not node: continue
		if visited == 0:
			stack.extend([(node.right, 0),(node, 1), (node.left, 0)])
		else:
			ans += node.val
			node.val = ans

	return root
			

