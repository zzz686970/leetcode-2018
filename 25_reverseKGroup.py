# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        ## l and r for the range
        ## return dummy.next
        jump = dummy = ListNode(0)
        dummy.next = l = r = head

        while True:
        	count = 0
        	while r and count < k:
        		r = r.next 
        		count += 1

        	## start reversing the linked list
        	if count == k:
        		## pre refers to the start element, cur is the first element of the next k group
        		pre, cur = l, r 
        		for _ in range(k):
        			pre.next, pre, cur = cur, pre.next, pre 
        			# temp = pre.next
        			# pre.next = cur
        			# cur = pre
        			# pre = temp

        		## after revering, reconnect the group
        		jump.next, jump, l = cur, l, r 
        		## segment
        		# jump.next = pre
        		# jump = l 
        		# l = r 
        	else:
        		return dummy.next 

