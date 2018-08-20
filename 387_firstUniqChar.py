def firstUniqChar(s):
	## can't ac
	# ans = ""
	# for i in range(len(s)):
	# 	if s.count(s[i]) == 1:
	# 		ans = i
	# 		break
	# if ans == 0 or ans:
	# 	return ans
	# return -1
	result = {}
	for char in s:
		result[char] = result[char] + 1 if char in result else 1

	for i in range(len(s)):
		if result[s[i]] == 1:
			return i

	return -1



s = "loveleetcode"
print(firstUniqChar(s))
