class TreeNode():
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class Solution:
	def leafSimilar(self, root1, root2):
		def getLeafs(root):
			if not root:
				return []
			if not root.left and not root.right:
				return [root.val]

			return getLeafs(root.left) + getLeafs(root.right)

		return getLeafs(root1) == getLeafs(root2)


