class Solution:
	def numMatchingSubseq(self, S, words):
		"""
		:type S: str
		:type words: List[str]
		:rtype: int
		"""
		## way 1
		cnt = 0
		for word in words:
			if len(word) >= len(S): cnt += (word == S) 
			start = 0
			for i in range(len(word)):
				start = S.find(word[i], start)
				if start == -1:
					break
				
				start += 1
			else:
				cnt += 1
		return cnt

		## way 2
		import collections
		import bisect

		res = collections.defaultdict(list)
		for index, val in enumerate(S): res[val].append(index)

		def check_word(w):
			j = 0
			for c in w:
				if c not in res or res[c][-1] < j:
					return False 
				j = res[c][bisect.bisect_left(res[c], j)] + 1

			return True 
		return sum(1 for w in words if check_word(w))


		