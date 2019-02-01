class Interval():
	def __init__(self, s=0, e = 0):
		self.start = s
		self.end = e

class Solution():
	def merge(self, intervals):
		ans = []
		for i in sorted(intervals, key= lambda x: x.start):
			if ans and i.start <= ans[-1].end:
				ans[-1].end = max(ans[-1].end, i.end)
			else:
				ans += i, 

		for el in ans:
			print(el.start, el.end)

		return ans 

a1 = Interval(1, 3)
a2 = Interval(2, 6)
a3 = Interval(8, 10)
a4 = Interval(15, 18)

a = Solution()

print(a.merge([a1, a2, a3, a4]))
# a.merge([[1,3],[2,6],[8,10],[15,18]])