def minAddToMakeValid(S):
	# while '()' in S:
	# 	S = S.replace('()','')

	# return len(S)

	l = r = 0
	for i in S:
		if r ==0 and i == ')': l += 1
		else: r += 1 if i == '(' else -1

	return l + r


assert 1 == minAddToMakeValid("((())")