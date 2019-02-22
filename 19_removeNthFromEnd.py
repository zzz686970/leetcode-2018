# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
		slow = fast = head
		## move ahead n
		for _ in range(n):
			fast = fast.next 

		if not fast:
			return head.next

		## now move slow and fast simultaneously
		## condition is fast.next so that slow would be in the positon which is before the removed element
		while fast.next:
			slow, fast = slow.next, fast.next 

		## remove the element 
		slow.next = slow.next.next 

		return head