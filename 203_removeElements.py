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



class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(-1)
        dummy_head.next = head 
        
        cur = dummy_head
        
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next 
        
        return dummy_head.next