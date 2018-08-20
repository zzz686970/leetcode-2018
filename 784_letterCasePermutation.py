import string
import itertools
def letterCasePermutation(S):
	rawlist = [char for char in S]
	list1 = [index for index, value in enumerate(S) if value not in str(string.digits)]
	result = dict()
	ans = []
	for i, value in enumerate(S):
		if value in string.ascii_letters:
			result[i] = [value.lower(), value.upper()]

	if result:
		for i, j in enumerate(list(itertools.product(*result.values()))):
			for a, b in zip(list1, range(len(j))):
				rawlist[a] = j[b]
			ans.append("".join(rawlist))
			# print(ans)
	else:
		ans.append(S)

	return ans


S = 'a1b'
print(letterCasePermutation(S))
# list(itertools.product([['a','b'],['A','B']]))