def countBinarySubstrings(s):
	# if len(s) == 1: return 0
	# count = -1
	# prev_el = None
	# rec1, rec2 = 0, 0
	# for el in s:
	# 	if prev_el == el:
	# 		rec1 += 1
	# 		if rec2 >= rec1:
	# 			count += 1
	# 	else:
	# 		rec2 = rec1
	# 		rec1 = 1
	# 		count += 1
	# 	prev_el = el

	# return count

	## way2
	result = []
	start = s[0]
	prev, last = 0, 0
	ans = 0
	for i in range(1, len(s)):
		index = i
		if s[i] == start:
			index += 1
		else:
			result.append([s[prev:index]])
			prev = i
			start = s[i]
	result.append([s[prev:]])
	for el in range(len(result)):
		if (el + 1) < len(result):
			ans += min(len(result[el][0]), len(result[el+1][0]))

	
	return ans

	# i = count = 0
	# l = len(s)
	# a, b = -1, 0
	# while i < l:
	# 	j = i + 1
	# 	while j < l and s[j] == s[i]:
	# 		j += 1
	# 	if a == -1:
	# 		a = j-i
	# 	else:
	# 		b = j -i
	# 		count += min(a, b)
	# 		a = b

	# 	i = j
	# return count 

s = "0000111"
print(countBinarySubstrings(s))
