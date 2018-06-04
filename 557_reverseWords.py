def reverseWords(s):
	result = []
	for char in list(s.split(" ")):
		new_char = "".join(list(reversed(char)))
		result.append(new_char)

	return " ".join(result)

print(reverseWords("Let's take LeetCode contest"))