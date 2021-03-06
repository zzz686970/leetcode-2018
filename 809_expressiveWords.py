def expressiveWords( S, words):
	"""
	:type S: str
	:type words: List[str]
	:rtype: int
	"""
	def separate(S):
		i = 0
		newS = ''
		while i < len(S)-1:
			if S[i] == S[i+1]:
				newS += S[i]
			else:
				newS +=  S[i] + ','
			i += 1
		if i == len(S)-1:
			newS += S[i] 

		return [(el[0], len(el)) for el in newS.split(',') if el]

	def compare(s, w):
		if len(s) != len(w):
			return False
		for a, b in zip(s, w):
			if a[0] == b[0]:
				if a[1] == b[1] or (a[1] >2 and a[1]> b[1]):
					continue
			return False 
		return True 

	newS = separate(S)
	return sum(compare(newS, separate(w)) for w in words)


	# def check(S, W):
	# 	i, j, n, m = 0, 0, len(S), len(W)
	# 	for i in range(n):
	# 		if j < m and S[i] == W[j]: j += 1
	# 		elif S[i - 1:i + 2] != S[i] * 3 != S[i - 2:i + 1]: return False
	# 	return j == m

	# return sum(check(S, W) for W in words)

	



print(expressiveWords("dddiiiinnssssssoooo",["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"]))
# print(expressiveWords("abcd", ["abc"]))
print(expressiveWords("heeellooo", ["hello", "hi", "helo"]))

