# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def detectCycle(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		slow, fast = head, head 
		while fast and fast.next:
			## need to change slow and fast first
			slow, fast = slow.next, fast.next.next 
			
			if slow == fast:
				break

			

		## find cycle, the second pass detect the head
		if fast and fast.next:
			p = head 
			while p and slow != p:
				p, slow = p.next, slow.next 

			return p 

		return None 