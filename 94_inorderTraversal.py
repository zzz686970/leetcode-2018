# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		##  recursive
  #   	if not root: return []
  #       else:
  #           return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
		
		ans = []
		def dfs(root):
			if not root: return 
			dfs(root.left)
			ans.append(root.val)
			dfs(root.right)
		dfs(root)

		return ans


		## iterative
		res, stack = [], []
		while stack or root:
			if root:
				stack.append(root)
				root = root.left 
			else:
				node = stack.pop()
				res.append(node.val)
				root = node.right 
		return res 