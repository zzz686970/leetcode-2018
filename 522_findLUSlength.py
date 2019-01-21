def findLUSlength(strs):
	def is_subsequence(s, t):
		print(s, "###", t)
		t = iter(t)
		# print(s, next(t), all(c in t for c in s))
		return all(c in t for c in s)

	for s in sorted(strs, key=len, reverse=True):
		if sum(is_subsequence(s, t) for t in strs) == 1:
			return len(s)

	return -1

print(findLUSlength(["aba", "cdc", "eaeaba"]))