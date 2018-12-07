# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def findTilt(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		self.ans = 0
		def sumup(node):
			if not node: return 0
			l, r = sumup(node.left), sumup(node.right)
			self.ans += abs(l - r)

			return node.val + l + r

		sumup(root)
		return self.ans