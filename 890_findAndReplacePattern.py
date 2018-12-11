def findAndReplacePattern(words, pattern):
	# result = []
	# for word in words:
	# 	chk = list(zip(word, pattern))
	# 	if len(set(pattern)) == len(set(word)) == len(set(chk)):
	# 		result.append(word)

	# return result

	return [word for word in words if len(set(pattern)) == len(set(word)) == len(set(list(zip(word, pattern))))]

print(findAndReplacePattern(words=["abc","deq","mee","aqq","dkd","ccc"], pattern='abb'))