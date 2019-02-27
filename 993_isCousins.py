# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
		stack = [(root, None)]

		## x, y need to be wrapped
		compare = sorted([x, y])
		while stack:
			new_stack = []
			for i in range(len(stack)-1):
				for j in range(i+1, len(stack)):
					## compare parent node and val
					if stack[i][1] != stack[j][1] and sorted([stack[i][0].val, stack[j][0].val]) == compare:
						return True 

			for node in stack:
				if node[0].left:
					new_stack.append((node[0].left, node[0]))
				if node[0].right:
					new_stack.append((node[0].right, node[0]))

			stack = new_stack

		return False 