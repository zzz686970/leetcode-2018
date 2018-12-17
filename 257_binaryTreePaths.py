#Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def binaryTreePaths(self, root):
		if not root: return []
		ans = []
		stack = [[root,'']]
		while stack:
			node, lf = stack.pop()
			if not node.left and not node.right:
				ans.append(lf + str(node.val))
			if node.left:
				stack.append([node.left, lf+str(node.val)+'->'])
			if node.right:
				stack.append([node.right, lf+str(node.val)+'->'])

		return ans 



node = ["node" + str(i + 1) for i in range(5)]
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
# node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3
# node2.left = node4
node2.right = node5

print(Solution().binaryTreePaths(node1)	 )