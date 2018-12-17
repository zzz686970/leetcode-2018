# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def levelOrderBottom(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if not root: return []
		result = []
		stack = [(root, 0)]
		while stack:
			node, level = stack.pop()
			if node:
				if len(result) < level + 1:
					result.insert(0,[])
				
				result[-(level+1)].append(node.val)
				stack.append((node.left, level+1))
				stack.append((node.right, level+1))
		return result


		