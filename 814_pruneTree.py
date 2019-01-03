def pruneTree(root):
	if not root: return root
	root.left, root.right = self.pruneTree(root.left), self.pruneTree(root.right)

	return root if root.val or root.left or root.right else None