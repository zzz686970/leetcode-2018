# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def largestValues(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		def bfs(self, root):
			self.ans = []
			if not root: return ans 
			queue = [root]
			while queue:
				ans.append(max(node.val for node in queue))
				new_queue = []
				for node in queue:
					if node.left:
						new_queue.append(node.left)
					if node.right:
						new_queue.append(node.right)
				queue = new_queue
			return self.ans


		### way2
		self.res = []
        if not root: return self.res 
        def dfs(root, level=0):
            if not root: return 
            if len(self.res) == level:
                self.res.append(root.val)
            else:
                self.res[level] = max(self.res[level], root.val)

            dfs(root.left, level+1)
            dfs(root.right, level+1)
        dfs(root, 0)
        return self.res

