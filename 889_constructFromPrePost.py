# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def constructFromPrePost(self, pre, post):
		"""
		:type pre: List[int]
		:type post: List[int]
		:rtype: TreeNode
		"""
		stack = [TreeNode(pre[0])]
		j = 0
		for v in pre[1:]:
			node = TreeNode(v)
			while stack[-1].val == post[j]:
				stack.pop()
				j += 1
			if not stack[-1].left:
				stack[-1].left = node 
			else:
				stack[-1].right = node

			stack.append(node)

		return stack[0]
