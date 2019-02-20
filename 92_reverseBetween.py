# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: 'ListNode', m: 'int', n: 'int') -> 'ListNode':

        ## create a dummy in case m==1 so there is a head change
        p = dummy = ListNode(0)
        dummy.next = head 

        ## position to m-1
        for _ in range(m-1):
            p = p.next

        pre = None
        cur = p.next 
        ## reverse the order between m and n
        for _ in range(n-m +1):
            cur.next, pre, cur = pre, cur, cur.next 

        ## after reverse, reconnect, cur becomes n+1, pre is n, but the reverse order is reserved
        p.next.next = cur 
        p.next = pre 

        return dummy.next 

