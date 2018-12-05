def isIsomorphic(s, t):
	ans = {}
	if len(set(s)) != len(set(t)):
		return False
	for a, b in zip(s, t):
		if a in ans and ans[a] != b:
			return False
		# elif b in ans and ans[b] != a:
		# 	return False
		else:
			ans[a] = b 



	return True

print(isIsomorphic('ab','ca'))



print(isIsomorphic('ab','aa'))