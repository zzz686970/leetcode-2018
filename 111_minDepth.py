# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def minDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root: return 0

		## each level is 1, for leaf node, there is no left and right
		## for root with one sub node, min(d) or max(d) will choose the valid path
		d = set(map(self.minDepth, (root.left, root.right)))
		return 1 + (min(d) or max(d))

		## way2
		# if not root: return 0
		# return 1 + min([self.minDepth(x) for x in (root.left,root.right) if x] or [0])  
		

		## way3	
	# 	return 0 if not root else self.dfs(root)
	# def dfs(self, root):
	# 	return 1 + min([self.dfs(x) for x in (root.left,root.right) if x] or [0])

	## way4  dfs
	def minDepth(self, root):
		if not root:
			return 0
		# res can be set as max_int
		res, stack = 9999, [(root, 1)]
		while stack:
			node, level = stack.pop()
			if node and not node.left and not node.right:
				res = min(res, level)
			if node:
				stack.append((node.left, level+1))
				stack.append((node.right, level+1))
		return res

	## way5 bfs

	def minDepth(self, root):
		if not root: return 0
		import collections
		queue = collections.deque([(root, 1)])
		while queue:
			node, level = queue.popleft()
			if node and not node.left and not node.right:
				return level
			elif node:
				queue.append((node.left, level+1))
				queue.append((node.right, level+1))
	