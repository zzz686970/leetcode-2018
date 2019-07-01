from functools import reduce
def removeDuplicates(S):
	ans = []
	for c in S:
		if ans and c == ans[-1]:
			ans.pop()
		else:
			ans.append(c)

	# return "".join(ans)

	## way 2
	## reduce(function, iterable, [initilizer,])
	return reduce(lambda s,c: s[:-1] if s[-1] == c else s + c, S, '#')[1:]

print(removeDuplicates("abbaca"))
