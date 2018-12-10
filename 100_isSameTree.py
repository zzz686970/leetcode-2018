def isSameTree(p, q):
	stack = [[p, q]]
	while stack:
		node1, node2 = stack.pop()
		if (not node1 and node2) or (node1 and not node2) or (node1 and node2 and node1.val != node2.val): return False
		if node1 and node2:
			stack.append([node1.left, node2.left])
			stack.append([node1.right, node2.right])

	return True