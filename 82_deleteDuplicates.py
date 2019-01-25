# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def deleteDuplicates(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		dummy = ListNode(0)
		dummy.next = head
		prev = dummy
		cur = head 
		while cur:
			if cur.next and cur.next.val == cur.val:
				while cur.next and  cur.next.val == cur.val:
					cur = cur.next 
				## temporary store the first value after duplicate numbers
				prev.next = cur.next
			else:
				prev = prev.next 
			cur = cur.next 
		return dummy.next