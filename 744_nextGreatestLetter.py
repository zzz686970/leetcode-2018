def nextGreatestLetter(letters, target):
	if not letters: return ''
	for letter in letters:
		if letter > target: return letter

	return letters[0]