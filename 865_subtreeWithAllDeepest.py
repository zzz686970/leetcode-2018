# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def subtreeWithAllDeepest(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		stack = [root] if root else []
		all_nodes = {}
		while stack:
			new_stack = []
			for node in stack:
				for child in (node.left, node.right):
					if child:
						## child --> parent
						all_nodes[child] = node
						new_stack.append(child)
			
			if not new_stack:
				break

			stack = new_stack

		## second bfs

		level = set(stack)
		while len(level) > 1:
			new_level = set(all_nodes[node] for node in level)
			level = new_level

		return level.pop()

	
	def subtreeWithAllDeepest(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		## one pass
		def dfs(root):
			if not root: return 0, None 
			l, r = dfs(root.left), dfs(root.right)
			if l[0] > r[0]: return l[0] + 1, l[1]
			elif l[0] < r[0]: return r[0]+1, r[1]
			else: return l[0] + 1, root 

			return dfs(root)[1]


		# 	tmp = set()
		# 	for node in all_nodes[pre:]
		# 		if node.left in deep or node.right in deep:
		# 			tmp.add(node)
		# 	deep = tmp 
		# 	pre -= 1

		# return next(iter(deep)) 