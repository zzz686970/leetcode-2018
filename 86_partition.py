# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def partition(self, head: 'ListNode', x: 'int') -> 'ListNode':
		## one for the left side, one for the right side
		h1 = l1 = ListNode(0)
		h2 = l2 = ListNode(0)

		while head:
			if head.val < x:
				l1.next = head 
				l1 = l1.next 
			else:
				l2.next = head 
				l2 = l2.next 

			head = head.next 

		## merge l1, l2
		l2.next = None 
		l1.next = h2.next 

		return h1.next 
