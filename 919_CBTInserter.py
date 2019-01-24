# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class CBTInserter:

	def __init__(self, root):
		"""
		:type root: TreeNode
		"""
		self.res = [root]
		for node in self.res:
			if node.left: self.res.append(node.left)
			if node.right: self.res.append(node.right)	

	def insert(self, v):
		"""
		:type v: int
		:rtype: int
		"""
		l = len(self.res)
		self.res.append(TreeNode(v))
		if l % 2:
			self.res[(l-1)//2].left = self.res[-1]
		else:
			self.res[(l-1)//2].right = self.res[-1]

		return self.res[(l-1)//2].val
		

	def get_root(self):
		"""
		:rtype: TreeNode
		"""
		return self.res[0]


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()