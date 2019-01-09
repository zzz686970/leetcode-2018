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

	## very slow
	# for idx, char in enumerate(s):
	# if s.count(char) == 1:
	# 	return idx
	# return -1

	## fastest
	chars = set(s)
	return min([s.index(el) for el in chars if s.count(el)==1] or [-1])

	import collections
	result = collections.defaultdict(int)
	# result = {}
	for char in s:
		# result[char] = result[char] + 1 if char in result else 1
		# result[char] = result.get(char, 0) + 1
		result[char] += 1

	for i in range(len(s)):
		if result[s[i]] == 1:
			return i

	return -1



s = "loveleetcode"
print(firstUniqChar(s))
