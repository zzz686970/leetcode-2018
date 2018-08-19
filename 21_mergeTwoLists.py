def mergeTwoLists(l1, l2):
	# if not l1 or not l2:
	# 	return l1 or l2

	# head = curr = ListNode(0)

	# while l1 and l2:
	# 	if l1.val < l2.val:
	# 		curr.next = l1
	# 		l1 = l1.next

	# 	else:
	# 		curr.next = l2
	# 		l2 = l2.next

	# 	curr = curr.next
	# curr.next = l1 or l2
	# return head.next

	if not l1 or not l2:
		return l1 or l2

	if l1.val < l2.val:
		l1.next = self.mergeTwoLists(l1.next, l2)
		return l1
	else:
		l2.next = self.mergeTwoLists(l1, l2.next)
		return l2
