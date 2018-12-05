class RecentCounter:

	def __init__(self):
		self.records = []
		self.result = []

	def ping(self, t):
		"""
		:type t: int
		:rtype: int
		"""
		self.records.append(t)
		for time in self.records:
			if time and 
		


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)