# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def invertTree(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		""" 
		if root:
			root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
			return root

		## way2
		# stack = [root]
		# while stack:
		# 	node = stack.pop()
		# 	if node:
		# 		node.left, node.right = node.right, node.left
		# 		stack += node.left, node.right
		# return root

if __name__ == "__main__":
	root = TreeNode(4)
	root.left = TreeNode(2)
	root.left.left = TreeNode(1)
	root.left.right = TreeNode(3)
	root.right = TreeNode(7)
	found = Solution().invertTree(root)
	print(found.val)



		
		