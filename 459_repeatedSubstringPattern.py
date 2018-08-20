def repeatedSubstringPattern(s):
	## can't ac
	for i in range(1, int(len(s)/2) + 1):
		if s.count(s[:i]) == len(s)/len(s[:i]):
			return True

	return False


s = 'aba'
print(repeatedSubstringPattern(s))