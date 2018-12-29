# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def rangeSumBST(self, root, L, R):
		"""
		:type root: TreeNode
		:type L: int
		:type R: int
		:rtype: int
		"""
		# if not root: return 0
		# l = self.rangeSumBST(root.left, L, R)
		# r = self.rangeSumBST(root.right, L, R)

		# return l + r + (L<= root.val <= R) * root.val

		## inorder
		return self.inorder(root, 0, L, R)

	def inorder(self, root, value, L, R):
		if root:
			value = self.inorder(root.left, value, L, R)
			if L <= root.val <= R:
				value += root.val 
			value = self.inorder(root.right, value, L, R)
		return value