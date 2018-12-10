class RecentCounter:

	def __init__(self):
		self.records = []
		self.index = 0
		self.cnt = 0

	def ping(self, t):
		"""
		:type t: int
		:rtype: int
		"""
		self.records.append(t)
		self.cnt += 1
		if t - self.records[self.index] > 3000:
			while  t-self.records[self.index] >3000:
				self.index += 1
				self.cnt -=1
		
		return self.cnt

		## timeout
		# index  = 0
		# if len(self.records) == 1: return 1
		# for i in range(len(self.records)):
		# 	if t - time <= 3000:
		# 		index = i 
		# 		break

		# return len(self.records) - index
		


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)