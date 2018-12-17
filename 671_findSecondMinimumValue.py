# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def findSecondMinimumValue(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		""" 
		stack = [root]
		ans = float('inf')
		min1 = root.val
		while stack:
			node = stack.pop()
			if not node: continue 
			else:
				if node.val == min1:
					stack.append(node.left)
					stack.append(node.right)
				elif min1 < node.val < ans:
					ans = node.val 
				
		return ans if ans < float('inf') else -1 

node1 = TreeNode(2)
node2 = TreeNode(2)
node3 = TreeNode(5)
node4 = TreeNode(5)
node5 = TreeNode(7)

node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

print(Solution().findSecondMinimumValue(node1))
		