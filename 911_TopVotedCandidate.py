class TopVotedCandidate:

	def __init__(self, persons, times):
		"""
		:type persons: List[int]
		:type times: List[int]
		"""
		self.res, self.times = [], times 
		cnt, win = {}, -1
		for t, p in zip(times, persons):
			cnt[p] = cnt.get(p, 0) + 1
			if cnt[p] >= cnt.get(win, 0): win = p
			self.res.append(win)



	def q(self, t):
		"""
		:type t: int
		:rtype: int
		"""
		return self.res[bisect.bisect(self.times, t)-1]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)