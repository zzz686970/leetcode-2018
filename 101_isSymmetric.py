def isSymmetric(root):
	if not root: return True
	stack = [[root.left, root.right]]
	while stack:
		l, r = stack.pop()
		if l is None and r is None:
			continue
		elif l is None or r is None:
			return False

		if l.val == r.val:
			stack.append([l.left, r.right])
			stack.append([l.right, r.left])
		else:
			return False

	return True