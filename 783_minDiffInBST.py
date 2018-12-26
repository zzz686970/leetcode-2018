# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def minDiffInBST(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		node, stack = root, []
		visited = None
		dist = float('inf')
		while stack or node:
			if node:
				stack.append(node)
				node = node.left 
			else:
				node =  stack.pop()
				if visited and node.val - visited.val < dist :
					dist = node.val - visited.val
				visited = node 
				node = node.right

		return dist