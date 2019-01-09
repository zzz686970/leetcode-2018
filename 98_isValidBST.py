# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def isValidBST(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		res = []
		def in_order(root):
			if not root:
				return
			in_order(root.left)
			res.append(root.val)
			in_order(root.right)

		in_order(root)
		for i in range(1,len(res)):
			if res[i-1] >= res[i]:
				return False
		return True