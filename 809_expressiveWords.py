def expressiveWords( S, words):
	"""
	:type S: str
	:type words: List[str]
	:rtype: int
	"""
	import collections
	
	d = collections.Counter(S)
	ans = len(words)
	for word in words:
		tmp = ''
		i = 0
		if not all(el in word for el in d) or len(word) > len(S): 
			ans-=1 
			break 
		while i < len(word):
			if word[i] not in d:
				ans -= 1
				break
			elif word[i] in d  and d[word[i]] < 3:
				val = d[word[i]]
				tmp = word[i] * val
				if tmp in word[i:i+val]:
					i += val -1
				else:
					ans -= 1
			else:
				# continue
				i += 1
			i += 1
	return ans

print(expressiveWords("dddiiiinnssssssoooo",["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"]))


