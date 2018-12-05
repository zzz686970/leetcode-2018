# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	## iteration
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		prev = None
		if not head: return None
		while head:
			head.next, prev, head = prev, head, head.next

		return prev

	## revursion

	def reverseList1(self, head, prev=None):
		if not head: return pre
		cur, head.next = head.next, pre
		
		return self.reverseList(cur, head)

