def wordPattern(pattern, str):
	result = dict()
	if len(set(pattern)) != len(set(str.split(" "))) or len(pattern) != len(str.split(" ")):
		return False
	for a, b in zip(pattern, str.split(" ")):
		if a in result and b != result[a]:
			return False
		else:
			result[a] = b
	return True

pattern = ""
str = "beef"
print(wordPattern(pattern, str))