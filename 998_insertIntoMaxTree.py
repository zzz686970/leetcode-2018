# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
		## cur node greater than inserted node, append to the right
		if root and root.val > val:
			root.right = self.insertIntoMaxTree(root.right, val)
			## need to return the value, which means cur node would not change
			return root
		## if inserted node is greater than current node
		node = TreeNode(val)
		## cur node changed to the left child of inserted ndoe
		node.left = root 

		return node