def lengthOfLastWord(s):
	result = [char for char in s.split(" ") if char]
	if not result:
		return 0
	return len(result[-1])
s = "Hello World"
print(lengthOfLastWord(s))