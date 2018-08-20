def countSegments(s):
	result = [char for char in s.split(" ") if char]
	if result == []:
		return 0
	else:
		return len(result)
	# result = []
	# cur = 0
	# if s == "":
	# 	return 0
	# for index, char in enumerate(s):
	# 	if s[index] == " " :
	# 		result.append(s[cur:index])
	# 		cur = index + 1
	# if s[cur:] != " ":
	# 	result.append(s[cur:])
	# return result

s = "                "
print(countSegments(s))