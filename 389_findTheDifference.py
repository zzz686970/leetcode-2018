def findTheDifference(s, t):
	## a , aa
	result = ""
	for char in t:
		if char not in s or s.count(char) != t.count(char):
			result = char
			break

	return result

	# newS = sorted(s)
	# newT = sorted(t)
	# for i in range(len(newS)):
	# 	if newS[i] in newT

s = 'a'
t = 'aa'
print(findTheDifference(s, t))
