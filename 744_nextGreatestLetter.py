def nextGreatestLetter(letters, target):
	if not letters: return ''
	for letter in letters:
		if letter > target: return letter

	return letters[0]

def nextGreatestLetter(letters, target):
	l, r = 0, len(letters)
	while l < r:
		mid = (l + r) // 2
		if letters[mid] > target:
			r = mid 
		elif letters[mid] <= target:
			l = mid + 1
	return letters[l%len(letters)]

assert "c" == nextGreatestLetter(["c", "f", "j"], 'a')
assert "f" == nextGreatestLetter(["c", "f", "j"], 'c')
assert "f" == nextGreatestLetter(["c", "f", "j"], 'd')
assert "j" == nextGreatestLetter(["c", "f", "j"], 'g')
assert "c" == nextGreatestLetter(["c", "f", "j"], 'j')
assert "c" == nextGreatestLetter(["c", "f", "j"], 'k')


