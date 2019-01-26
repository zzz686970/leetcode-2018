def replaceWords(dict, sentence):
	if not dict or not sentence: return sentence
	res = []
	pairs = sorted(dict, key=len)
	for word in sentence.split(' '):
		for pair in pairs:
			if pair in word[:len(pair)]:
				res.append(pair)
				break  
		else:
			res.append(word)

	return " ".join(res)

print(replaceWords(dict = ["cat", "bat", "rat"],
sentence = "the cattle was rattled by the battery"))

print(replaceWords(["a","b","c"],
"aadsfasf absbs bbab cadsfafs"))