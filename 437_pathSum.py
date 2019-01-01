# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def pathSum(self, root, sum):
		"""
		:type root: TreeNode 
		:type sum: int
		:rtype: int
		"""
		self.num_path = 0
		self.dfs(root, sum)
		return self.num_path

	def dfs(node, target):
		if not node: return 
		self.test(node, target)
		self.dfs(node.left, target)
		self.dfg(node.right, target)

	def test(node, target):
		if not node: return 
		if node.val == target:
			self.num_path += 1
		self.test(node.left, target-node.val)
		self.test(node.right, target-node.val)

class Solution1:
	def pathSum(self, root, sum):
		self.result = 0
		cache = {0, 1}
		self.dfs(root, sum, 0, cahce)

		return self.result 

	def dfs(self, root, target, curr_path, cache):
		if not root: return
		curr_path += root.val 
		prev_path = curr_path - target 
		self.result += cache.get(prev_path, 0)
		cache[curr_path] = cache.get(curr_path, 0) + 1

		self.dfs(root.left, target, curr_path, cache)
		self.dfs(root.right, target, curr_path, cache)
		cache[curr_path] -= 1





