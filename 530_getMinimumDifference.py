# def getMinimumDifference(root):
# 	if not root: return 0
# 	stack = [root]
# 	while stack:
# 		node = stack[-1]
# 		if node.left:
# 			stack.append(node.left)
# 		if node.right:
# 			stack.append(node.right)

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def getMinimumDifference(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		node, stack = root, []
		visited = None
		dist = float('inf')
		while stack or node:
			if node:
				stack.append(node)
				node = node.left 
			else:
				node =  stack.pop()
				if visited and node.val - visited.val < dist :
					dist = node.val - visited.val
				visited = node 
				node = node.right

		return dist




		## way2
		if not root: return 0
		stack = [root]
		# res = []
		ans = float('inf')
		prev = None
		while stack:
			node = stack[-1]
			if node.left:
				stack.append(node.left)
				node.left = None
			else:
				node = stack.pop()
				# res.append(node.val)
				if prev and node.val - prev.val < ans:
					ans = node.val - prev.val 
				prev = node
				if node.right: 
					stack.append(node.right)
					node.right = None
		return ans 

node1 = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(6)
node4 = TreeNode(3)
node5 = TreeNode(1)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

a = Solution()
print(a.getMinimumDifference(node1))


