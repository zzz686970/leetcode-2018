def findWords(words):
	row1 = 'qwertyuipo'
	row2 = 'asdfghjkl'
	row3 = 'zxcvbnm'
	result = []

	for word in words:
		if all(char.lower() in row2 for char in word) or all(char.lower() in row1 for char in word) or all(char.lower() in row3 for char in word):
			result.append(word)
	
	return result

words = ["Hello", "Alaska", "Dad", "Peace"]
print(findWords(words))
			
