# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """ 
        ans = {}
        m = n = head 
        while m:
            ans[m] = RandomListNode(m.label)
            m = m.next 

        while n:
            ans[n].next = ans.get(n.next)
            ans[n].random = ans.get(n.random)
            n = n.next 

        return ans.get(head)

## O(N) solution
import collections
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """ 
        ans = collections.defaultdict(lambda: RandomListNode(0))
        ans[None] = None
        m = head 
        while m:
            ans[m].label = m.label
            ans[m].next = ans[m.next]
            ans[m].random = ans[m.random]
            m = m.next 

        
        return ans.get(head)