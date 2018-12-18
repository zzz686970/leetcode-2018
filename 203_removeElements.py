# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def removeElements(self, head, val):
		"""
		:type head: ListNode
		:type val: int
		:rtype: ListNode
		"""
		if not head: return []
		while head and head.val == val: head = head.next
		curr = head
		while curr:
			if curr.next.val == val:
				curr.next = curr.next.next
			else:
				curr = curr.next 

		return head