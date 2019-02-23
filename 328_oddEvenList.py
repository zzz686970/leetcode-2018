# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def oddEvenList(self, head: 'ListNode') -> 'ListNode':
		h1 = odd = ListNode(0)
		h2 = even = ListNode(0)
		while head:
			## wrong code, must reference first
			# odd.next, odd = head, odd.next 
			# even.next, even = head.next, even.next
			odd.next, even.next = head, head.next
			odd, even = odd.next, even.next
			head = head.next.next if even else None 

		## merge
		## no need to set even.next again
		# even.next = None 
		odd.next = h2.next

		return h1.next