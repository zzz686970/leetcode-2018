def findAnagrams(s, p):
	from collections import Counter
	ls, lp = len(s), len(p)
	count = lp
	cp = Counter(p)
	result = []
	for i in range(ls):
		print(s[i])
		if cp[s[i]] >=1:
			count -= 1
		cp[s[i]] -= 1

		if i >= lp:
			if cp[s[i-lp]] >= 0:
				count += 1
			cp[s[i-lp]] += 1

		if count == 0:
			result.append(i - lp + 1)

	return result

	# result = []
	# index = 0
	# unvisted = [i for i in p]
	# for i in range(len(s)):
	# 	for j in range(len(p)):
	# 		if p[j] == s[i] and p[j] in unvisted:
	# 			index += 1
	# 			unvisted[j] = '0'

	# 			break
	# 	if index < len(p):
	# 		unvisted
	# 	elif index == len(p):
	# 		result.append(i-len(p)+1)
	# 		index = 0
	# 		unvisted = [el for el in p]
	# 		# unvisted[j] = '0'
	# 		# print(unvisted)
			
	# return result

s = "cabab"
p = "ab"
print(findAnagrams(s, p))