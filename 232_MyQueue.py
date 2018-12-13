# class MyQueue:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.result = []

#     def push(self, x):
#         """
#         Push element x to the back of queue.
#         :type x: int
#         :rtype: void
#         """
#         self.result.append(x)
        

#     def pop(self):
#         """
#         Removes the element from in front of queue and returns that element.
#         :rtype: int
#         """
#         self.result.pop(0)
#         return self.result
        

#     def peek(self):
#         """
#         Get the front element.
#         :rtype: int
#         """
#         return self.result[0]
        

#     def empty(self):
#         """
#         Returns whether the queue is empty.
#         :rtype: bool
#         """
#         return False if self.result else True


# # Your MyQueue object will be instantiated and called as such:
# # obj = MyQueue()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.peek()
# # param_4 = obj.empty()

class Queue(object):
	def __init__(self):
		self.input = []
		self.output = []
	def push(self, x):
		self.input.append(x)

	def pop(self):
		self.peek()
		return self.output.pop()

	def peek(self):
		if(self.output==[]):
			while(self.input != []):
				self.output.append(self.input.pop())
		return self.output[-1]

	def empty(self):
		reutrn self.input == [] and self.output == []