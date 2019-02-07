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


def replaceWords(dict, sentence):
	if not dict or not sentence: return sentence
	res_dict = {i:len(i) for i in dict}
	res_value= list(set(res_dict.values()))
	res_value.sort()

	words = sentence.split(' ')
	for i, word in enumerate(words):
		for j in res_value:
			if word[:j] in res_dict:
				words[i] = words[:j]
				break 

	return ' '.join(words)



