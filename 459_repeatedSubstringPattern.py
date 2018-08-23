def repeatedSubstringPattern(s):
	## ac but slow
	# for i in range(1, int(len(s)/2) + 1):
	# 	if len(s) % i:
	# 		continue
	# 	if s[:i] * int(len(s) / i) == s:
	# 		return True

	# return False
	size = len(s)
	next = [0] * size
	for i in range(1, size):
		k = next[i-1]
		print(next)
		while s[i] != s[k] and k:
			k = next[k-1]

		if s[i] == s[k]:
			next[i] = k+1

	p = next[-1]


	return p>0 and size % (size-p) == 0

s = 'abcdabcabcdabcdc'
print(repeatedSubstringPattern(s))