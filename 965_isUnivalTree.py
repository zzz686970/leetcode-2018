class Solution:
	def isUnivalTree(root):
		if not root: return True

		if (root.left and root.val != root.left.val) or (root.right and root.val != root.right.val):
			return False

		return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)

	def isUnivalTree(root):
		stack = [root]
		cur = root.val 
		while stack:
			node = stack.pop()
			if node.val != cur:
				break 
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)
		## else is used to check whether the loop ends from a break or actual ends
		else:
			return True 
		return False