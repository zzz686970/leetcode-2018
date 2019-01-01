"""
# Definition for a QuadTree node.
"""
class Node:
	def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
		self.val = val
		self.isLeaf = isLeaf
		self.topLeft = topLeft
		self.topRight = topRight
		self.bottomLeft = bottomLeft
		self.bottomRight = bottomRight

class Solution:
	def intersect(self, q1, q2):
		"""
		:type quadTree1: Node
		:type quadTree2: Node
		:rtype: Node
		"""
		if q1.isLeaf:
			return q1.val and q1 or q2
		elif q2.isLeaf:
			return q2.val and q2 or q1
		else:
			t_left = self.intersect(q1.topLeft, q2.topLeft)
			t_right = self.intersect(q1.topRight, q2.topRight)
			b_left = self.intersect(q1.bottomLeft, q2.bottomLeft)
			b_right = self.intersect(q1.bottomRight, q2.bottomRight)
			# vals = [t.val for t in (t_left,t_right,b_left,b_right) if t.isLeaf]
			# if vals and vals.count(vals[0]) == len(vals) == 4:
			if all(el.isLeaf and t_left.val==el.val for el in (t_left,t_right,b_left,b_right)):
				node = Node(t_left.val, True, None, None, None, None)
			else:
				node = Node(False, False, t_left, t_right, b_left, b_right)

			return node 

