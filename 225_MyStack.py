class MyStack(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		import collections
		self.queue = collections.deque()

	def push(self, x):
		"""
		Push element x onto stack.
		:type x: int
		:rtype: void
		"""
		## each time an element is pushed into the stack, reverse the queue 1,2 -> 2, 1; then another push would be 2, 1, 3 -> 3, 2, 1
		self.queue.append(x)
		for _ in range(len(self.queue)-1):
			self.queue.append(self.queue.popleft())

	def pop(self):
		"""
		Removes the element on top of the stack and returns that element.
		:rtype: int
		"""
		return self.queue.popleft()

	def top(self):
		"""
		Get the top element.
		:rtype: int
		"""
		return self.queue[0]

	def empty(self):
		"""
		Returns whether the stack is empty.
		:rtype: bool
		"""
		return not len(self.queue)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()