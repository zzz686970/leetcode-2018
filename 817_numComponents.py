def numComponents(head, G):
	G = set(G)
	res = 0
	while head:
		if head.val in G and (head.next is None or head.next.val not in G):
			res += 1

		head = head.next 

	return res