def removeKdigits(num, k):
	ans = []
	for d in num:
		while k and ans and ans[-1]>d:
			ans.pop()
			k -= 1
		ans.append(d)

	return "".join(ans[:-k or None]).lstrip('0') or '0'