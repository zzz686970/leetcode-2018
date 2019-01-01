class Solution:
	def isUnivalTree(root):
		if not root: return True

		if (root.left and root.val != root.left.val) or (root.right and root.val != root.right.val):
			return False

		return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)