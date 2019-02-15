def mergeKLists(lists):
	nodelist = []
	for i in range(len(lists)):
		curr_node = lists[i]
		while curr_node:
			nodelist.append(cur_node)
			curr_node = curr_node.next 

	nodelist = sorted(nodelist, key=lambda x: x.val)

	temp = ListNode(0)
	cur = temp 
	for i in range(len(nodelist)):
		cur.next = nodelist[i]
		cur = cur.next 

	return temp.next 


import heapq
def mergeKLists(lists):
	heap = []
	for node in lists:
		if node != None:
			heap.append((node.val, node))

	heapq.heapify(heap)
	head = ListNode(0)
	curr = head 
	while heap:
		pop = heapq.heappop(heap)
		curr.next = ListNode(pop[0])
		curr = curr.next 
		if pop[1].next:
			heapq.heappush(heap, (pop[1].next.val, pop[1].next))

	return head.next 

