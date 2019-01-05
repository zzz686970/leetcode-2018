from bisect import insort
class MyCalendarThree:

	def __init__(self):
		self.times=[]

	def book(self, start, end):
		"""
		:type start: int
		:type end: int
		:rtype: int
		"""
		insort(self.times, (start, 1))
		insort(self.times, (end,-1))
		accumulate = res = 0
		for _, x in self.times:
			accumulate += x
			res = max(res, accumulate)

		return res 

MyCalendarThree = MyCalendarThree()
print(MyCalendarThree.book(10, 20)); # returns 1
print(MyCalendarThree.book(50, 60)); # returns 1
print(MyCalendarThree.book(10, 40)); # returns 2
print(MyCalendarThree.book(5, 15)); # returns 3
print(MyCalendarThree.book(5, 10)); # returns 3
print(MyCalendarThree.book(25, 55)); # returns 3
		
# [(10, 1), (20, -1)]
# [(10, 1), (20, -1), (50, 1), (60, -1)]
# [(10, 1), (10, 1), (20, -1), (40, -1), (50, 1), (60, -1)]
# [(5, 1), (10, 1), (10, 1), (15, -1), (20, -1), (40, -1), (50, 1), (60, -1)]
# [(5, 1), (5, 1), (10, -1), (10, 1), (10, 1), (15, -1), (20, -1), (40, -1), (50, 1), (60, -1)]
# [(5, 1), (5, 1), (10, -1), (10, 1), (10, 1), (15, -1), (20, -1), (25, 1), (40, -1), (50, 1), (55, -1), (60, -1)]

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)