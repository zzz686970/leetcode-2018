def longestWord(words):
	new = sorted(words)
	word_set, result = set(['']),''
	for word in new:
		if word[:-1] in word_set:
			word_set.add(word)
			if len(word) > len(result):
				result = word

	return result

print(longestWord(["w","wo","wor","worl", "world"]))

assert 'apple' == longestWord(words = ["a", "banana", "app", "appl", "ap", "apply", "apple"])