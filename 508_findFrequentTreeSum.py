# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def findFrequentTreeSum(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		self.res = {}
		self.max_val = 0
		ans = []
		def dfs(root):
			if not root: return 0
			l, r = dfs(root.left), dfs(root.right)

			total = root.val + l + r 

			if total not in self.res:
				self.res[total] = 1
			else:
				self.res[total] += 1

			self.max_val = max(self.res[total], self.max_val)

			return total 

		dfs(root)
		for i in self.res:
			if self.res[i] == self.max_val:
				ans.append(i)

		return ans 