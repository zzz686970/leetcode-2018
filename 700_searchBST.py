class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def searchBST(self, root, val):
		"""
		:type root: TreeNode
		:type val: int
		:rtype: TreeNode
		""" 
		if not root: return None
		if isinstance(root, int) and root != val: return None
		if root.val == val:
			return root
		left = self.searchBST(root.left, val)
		right = self.searchBST(root.right, val)
		return left if left else right


if __name__ == "__main__":
	root = TreeNode(4)
	root.left = TreeNode(2)
	root.left.left = 1
	root.left.right = 3
	root.right = 7
	found = Solution().searchBST(root, 2)
	print(found.val)
	print(found.left)
	print(found.right)

