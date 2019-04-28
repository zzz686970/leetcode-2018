def removeOuterParentheses(S):
	if not S: return ''
	l, r, ans  = 0, 0, ''
	cnt = 0
	for idx, ch in enumerate(S):
		if ch == '(':
			cnt += 1
		elif ch == ')':
			cnt -= 1

		if cnt == 0:
			r = idx
			ans += S[l+1:r]
			l = idx+1
	return ans if ans else ""

print(removeOuterParentheses("()()"))

