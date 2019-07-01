def sumRootToLeaf(root, val = 0):
	if not root: return 0 
	val = 2 * val + root.val 
	## if leaf node, left==right == None
	if root.left == root.right: return val 
	return self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val) 
