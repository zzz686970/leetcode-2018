def new21Game(N, K, W):
	import itertools
	if K == 0 or N >= K + W: return 1
	pool = [i for i in range(1, W+1)]
	all_res = list(itertools.combinations(pool, K))
	# print('1', all_res)
	# print([sum(el) for el in all_res if sum(el) <= N ])
	return len([sum(el) for el in all_res if sum(el) <= N ]) / len(list(all_res))

	## possibility is guaranteed 
	# if K == 0 or N >= K + W: return 1

	# dp = [1.] + 0. * [N]
	# total = 1.
	# for i in range(1, N+1):
	# 	dp[i] = total / W 
	# 	if i < K : total += dp[i]
	# 	if i-W >=0: total -= dp[i]

	# return sum(dp[K:])

	# point = 0
	# pool = set(i for i in range(W))
	# while point < K:
	# 	cur = pool.pop()
	# 	point += 1

	# return 

# print(new21Game(N = 10, K = 1, W = 10))
print(new21Game(N = 6, K = 1, W = 10))
# print(new21Game(N = 21, K = 17, W = 10))