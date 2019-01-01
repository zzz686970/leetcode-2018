class Solution:
	def hasPathSum(self, root, sum):
		if not root: return False
		if root and not root.left and not roo.right and root.val == sum:
			return True 
		return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

	def hasPathSum(self, root, sum):
		stack = [(root, sum)]
		while stack:
			node, value = stack.pop()
			if node:
				if not node.left and not node.right and node.val == value:
					return True 
				stack.append((node.left, value-node.value))
				stack.append((node.right, value-node.value))

			else:
				continue 

		return False