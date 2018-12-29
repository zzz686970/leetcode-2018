# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def lowestCommonAncestor(self, root, p, q):
		"""
		:type root: TreeNode
		:type p: TreeNode
		:type q: TreeNode
		:rtype: TreeNode
		"""
		while root:
			p_val, q_val, r_val = p.val, q.val, root.val 
			if r_val > max(p_val, q_val): root = root.left
			elif r_val < min(p_val, q_val): root = root.right 
			else: return root