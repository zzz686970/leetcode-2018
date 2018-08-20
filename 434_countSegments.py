def countSegments(s):
	result = []
	cur = 0
	if s == "":
		return 0
	for index, char in enumerate(s):
		if s[index] == " " :
			result.append(s[cur:index])
			cur = index + 1
	if s[cur:] != " ":
		result.append(s[cur:])
	return result

s = "                "
print(countSegments(s))