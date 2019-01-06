# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def rightSideView(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		""" 
		res = []

		def dfs(root, level):
			if root:
				if level == len(res):
					res.append(root.val)
				dfs(root.right, level+1)
				dfs(root.left, level+1)

		dfs(root, 0)
		return res

		## way2
		# res = []
		# level = [root]
		# if root:
		# 	while level:
		# 		res += level[-1].val,
		# 		level = [kid for node in level for kid in (node.left, node.right) if kid]
		# return res 

		## way3
		# if not root:
		# 	return []
		# right = self.rightSideView(root.right)
		# left = self.rightSideView(root.left)
		# return [root.val] + right + left[len(right):]

