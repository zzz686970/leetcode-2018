class Solution():
	def getIntersectionNode(self, headA, headB):
		if headA is None or headB is None:
			return None
		a, b = headA, headB
		while a is not b:
			a = headB if a is None else a.next
			b = headA if b is None else b.next

		return a