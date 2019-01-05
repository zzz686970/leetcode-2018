# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def findBottomLeftValue(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		queue = [root]
		for node in queue:
			if node.right:
				queue.append(node.right)
			if node.left:
				queue.append(node.left)

		return queue[-1].val


		# queue = [root]
		# for node in queue:
		# 	queue += filter(None, (node.right, node.left))
		
		# ## notice node is not destroyed
		# return node.val