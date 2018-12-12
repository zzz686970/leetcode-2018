def backspaceCompare(S,T):
	newS, newT = '', ''

	def getNew(st):
		newC = ''
		for c in st:
			if c !='#':
				newC += c
			else:
				newC = newC[:-1]

		return newC
		

	newS, newT = getNew(S), getNew(T)
	print(newS, newT)

	return newS == newT

print(backspaceCompare(S='ab##',T='c#d#'))

