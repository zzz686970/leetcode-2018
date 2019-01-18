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
		