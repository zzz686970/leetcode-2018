def combinationSum3(k, n):
	## itertools
	import itertools 
	return [list(c) for c in itertools.combinations(range(1, 10), k) if sum(c)==n]

	# res = []
	# for i in range(n):
	# 	target = n - i 

	## second 
	# def dfs(target, k):
	# 	if k == 0:
	# 		return target
	# 	for i in range(target):
	# 		new_target = target - i 

	# 		dfs(new_target, k-1)

print(combinationSum3(k = 3, n = 7))