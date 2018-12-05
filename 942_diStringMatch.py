def diStringMatch(S):
	l, r, result = 0, len(S), []
	for s in S:
		result.append(l if s == 'I' else r)
		## s == 'I' would be 0 or 1
		l, r = l + (s =='I'), r-(s =='D')

	## same as result + [r]
	return result + [l]

print(diStringMatch('IID'))