def increasingBST(root, tail = None):
	if not root: return tail
	ans = self.increasingBST(root.left, root)
	root.left = None
	root.right = self.increasingBST(root.right, tail)
	return ans


