import itertools
def solution(N):
	num, l = str(N), len(str(N))
	ans = set()
	for i in itertools.permutations(num, l):
		if len(str(int("".join(i)))) == l:
			ans.add(int("".join(i)))

	return len(ans)

print(solution(1213))