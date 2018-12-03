# Definition for singly-linked list.

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def isPalindrome(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		## (O(n) space)
		if not head: return None
		result = []
		while head:
			result.append(head.val)
			head = head.next
		
		return result == result[::-1]

		## O(1) space

	def isPalindrome2(self, head):
		# rev records the first half, need to set the same structure as fast, slow, hence later we have rev.next
		rev = None
		# initially slow and fast are the same, starting from head
		fast  = slow =  head
		while fast and fast.next:			
	
			# fast traverses faster and moves to the end of the list if the length is odd
			fast = fast.next.next		
			# take it as a tuple being assigned (rev, rev.next, slow) = (slow, rev, slow.next), hence the re-assignment of slow would not affect rev (rev = slow)
			rev, rev.next, slow = slow, rev, slow.next
			
		if fast:
		   # fast is at the end, move slow one step further for comparison(cross middle one)
			slow = slow.next
		# compare the reversed first half with the second half
		while rev and rev.val == slow.val:
			slow = slow.next
			rev = rev.next
		
		# if equivalent then rev become None, return True; otherwise return False 
		return not rev


if __name__ == '__main__':
	from _utils import linkedList
	a_list = [2,3,5,3,1]
	# Node1, Node2, Node3, Node4, Node5 = ListNode(1), ListNode(2), ListNode(3), ListNode(2), ListNode(1)
	# Node1.next = Node2
	# Node2.next = Node3
	# Node3.next = Node4
	# Node4.next = Node5
	

	# newList = linkedList(a_list)
	# print(newList.head.val)

	a = Solution()

	print(a.isPalindrome2(newList.head))




