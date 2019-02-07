import itertools
def combine(n: 'int', k: 'int'):
	# return [list(c) for c in itertools.combinations(range(1, n+1), k)]

	## iterative
	combs = [[]]
	for j in range(k, 0, -1):
		combs = [[i]+c for c in combs for i in range(j, c[0] if c else n+1)]
		print(combs)

	return combs

print(combine(n=4, k = 3))