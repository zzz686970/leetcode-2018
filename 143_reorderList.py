# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def reorderList(self, head: 'ListNode') -> 'None':
		"""
		Do not return anything, modify head in-place instead.
		"""
		slow = fast = head 
		while fast and fast.next:
			slow, fast = slow.next, fast.next.next 

		pre, cur = None, slow 
		## reverse the second half
		while cur:
			cur.next, pre, cur = pre, cur, cur.next 

		## pre is the last element, but with reverse order
		first, second = head, pre 
		while second.next:
			first.next, first = second, first.next 
			second.next, second = first, second.next 

		return 