# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        head = ListNode(0)
        print(s1, s2)
        while s1 or s2 or carry:
            if s1:
                carry += s1.pop()
            if s2:
                carry += s2.pop()
            carry, val = divmod(carry, 10)
            head.next, head.next.next = ListNode(val), head.next

        print(head.next.val)
        return head.next

if __name__ == '__main__':
	a = Solution()
	l1 = ListNode(7)
	l1.next = ListNode(2)
	l1.next.next = ListNode(4)
	l1.next.next.next = ListNode(3)

	l2 = ListNode(5)
	l2.next = ListNode(6)
	l2.next.next = ListNode(4)


	print(a.addTwoNumbers(l1, l2))