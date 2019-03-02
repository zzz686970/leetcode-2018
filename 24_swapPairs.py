# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, prev.next = self, head 
        while prev.next and prev.next.next:
            a = prev.next 
            b = a.next 
            ## exchange pre-> a -> b -> b.next to pre -> b -> a -> b.next
            prev.next, b.next, a.next = b, a, b.next 

            prev = a 

        return self.next 

    def swapPairs1(self, head):
        dummy = pre =  ListNode(0)
        pre.next = head 
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next 
            pre.next, a.next, b.next = b, b.next, a 
            pre = a 

        return dummy.next 