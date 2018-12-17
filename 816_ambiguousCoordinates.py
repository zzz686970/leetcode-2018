def ambiguousCoordinates(S):
	import itertools
	S = S[1:-1]

	def sub(s):
		if s=='' or (len(s) > 1 and s[0]==s[-1]=='0'): return []
		if s[-1]=='0': return [s]
		if s[0]=='0': return [s[0]+'.'+s[1:]]
		return [s]+[s[:i] +'.' +s[i:] for i in range(1, len(s))]

	return ['(%s, %s)'%(a,b) for i in range(len(S)) for a, b in itertools.product(sub(S[:i]), sub(S[i:]))]	


print(ambiguousCoordinates("(0123)"))