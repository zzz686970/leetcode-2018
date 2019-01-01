class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class Solution(object):
	def isBalanced(self, root):
		self.ans = True
		def dfs(root, level = 0):
			if not root: return level
			level += 1
			a, b = dfs(root.left, level), dfs(root.right, level)
			if abs(a-b) > 1: self.ans = False

			return max(a, b)
		dfs(root)
		return self.ans
	# def isBalanced(self, root):	
	# 	def check(root):
	# 		if root is None:
	# 			return 0
	# 		left  = check(root.left)
	# 		right = check(root.right)
	# 		if left == -1 or right == -1 or abs(left - right) > 1:
	# 			return -1
	# 		return 1 + max(left, right)
			
	# 	return check(root) != -1

		

