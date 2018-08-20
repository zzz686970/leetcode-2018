import string
def titleToNumber(s):
	result = dict()
	ans = 0
	for a, b in zip(string.ascii_uppercase, range(1, 27)):
		result[a] = b
	for index, char in enumerate(reversed(s)):
		# print(index, char)
		if index == 0:
			ans += result[char]
		else:
			ans += (26 ** index) * result[char]


	return ans

s = "AAA"
print(titleToNumber(s))