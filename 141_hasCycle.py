# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def hasCycle(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		if not head: return False
		slow, fast = head, head.next
		while slow is not fast:
			if slow is None or fast is None or fast.next is None:
				return False 
			slow, fast = slow.next, fast.next.next 

		return True