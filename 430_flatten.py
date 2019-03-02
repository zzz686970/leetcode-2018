"""
# Definition for a Node.
"""
class Node:
	def __init__(self, val, prev, next, child):
		self.val = val
		self.prev = prev
		self.next = next
		self.child = child
class Solution:
	def flatten(self, head) -> 'Node':
		if not head: return 
		dummy = Node(0, None, head, None)
		stack = [head]
		prev = dummy 
		while stack:
			node = stack.pop()
			node.prev, prev.next = prev, node 

			if node.next:
				stack.append(node.next)
				node.next = None 
			if node.child:
				stack.append(node.child)
				node.child = None 

			prev = node 
		
		## remove the prev connection of dummy and head
		dummy.next.prev = None 

		return dummy.next