# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def sumOfLeftLeaves(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		# self.ans = 0
		# if not root: return 0
		# def dfs(node):
		# 	if not node: return 0
		# 	l, r = dfs(node.left), dfs(node.right)
		# 	self.ans += l 

		# 	return node.val

		# dfs(root)
		# return self.ans
		if not root: return 0
		self.ans = 0
		stack = [root]
		while stack:
			node = stack.pop()
			if node.left:
				stack.append(node.left)
				if not node.left.right and not node.left.left:
					self.ans += node.left.val
			if node.right:
				stack.append(node.right)

		return self.ans

node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)
node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5
a = Solution()
print(a.sumOfLeftLeaves(node1))


