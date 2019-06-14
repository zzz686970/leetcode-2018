def removeDuplicates(S):
	i, ans = 0, ''
	if len(S) == 1: return 1
	else:
		while i < len(S)-1:
			if S[i] == S[i+1]:
				i += 1
			else:
				ans += S[i]
