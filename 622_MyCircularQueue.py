class Node:
	def __init__(self, val):
		self.val = val 
		self.next = self.prev = None

class MyCircularQueue:

	def __init__(self, k):
		"""
		Initialize your data structure here. Set the size of the queue to be k.
		:type k: int
		"""
		self.size = k
		self.cur_size = 0
		self.head = self.tail = Node(-1)
		self.head.next = self.tail 
		self.tail.prev = self.head 

	def enQueue(self, value):
		"""
		Insert an element into the circular queue. Return true if the operation is successful.
		:type value: int
		:rtype: bool
		"""
		if self.cur_size < self.size:
			node = Node(value)
			node.prev = self.tail.prev 
			node.next = self.tail
			node.prev.next = node.next.prev = node 
			self.cur_size += 1
			return True 

		return False 
		

	def deQueue(self):
		"""
		Delete an element from the circular queue. Return true if the operation is successful.
		:rtype: bool
		"""
		if self.cur_size > 0:
			node = self.head.next
			# self.head.next = node.next 
			node.prev.next = node.next 
			node.next.prev = node.prev 
			self.cur_size -= 1
			return True 
		return False

	def Front(self):
		"""
		Get the front item from the queue.
		:rtype: int
		"""
		return self.head.next.val

	def Rear(self):
		"""
		Get the last item from the queue.
		:rtype: int
		"""
		return self.tail.prev.val

	def isEmpty(self):
		"""
		Checks whether the circular queue is empty or not.
		:rtype: bool
		"""
		return self.cur_size == 0

	def isFull(self):
		"""
		Checks whether the circular queue is full or not.
		:rtype: bool
		"""
		return self.cur_size == self.size 


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()