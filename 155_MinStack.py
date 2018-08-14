class MinStack:

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.stack = []
		

	def push(self, x):
		"""
		:type x: int
		:rtype: void
		"""
		init_min = 2147483647 if len(self.stack) == 0 else self.stack[-1][1]
		cur_min = min(x, init_min)
		self.stack.append((x, cur_min))
		

	def pop(self):
		"""
		:rtype: void
		"""
		self.stack.pop()
		

	def top(self):
		"""
		:rtype: int
		"""
		return self.stack[-1][0]

		

	def getMin(self):
		"""
		:rtype: int
		"""
		return self.stack[-1][1]
		


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()