class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution():
    def getDecimalValue(self, head) -> int:
        ans = 0
        while head:
            ans = ans << 1 | head.val
            head = head.next
        return ans
