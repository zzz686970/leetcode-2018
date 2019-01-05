def dailyTemperatures(T):
	res = [0 for _ in range(len(T))]
	stack = []
	for i, t in enumerate(T):
		while stack and T[stack[-1]] < t:
			cur = stack.pop()
			res[cur] = i - cur 

		stack.append(i)

	return res

	## hash map
	# res = [0 for _ in range(len(T))]
	# days = {}
	# for i in range(len(T)-1, -1, -1):
	# 	days[T[i]] = i 
	# 	cnt = [day for ind, day in days.items() if ind > T[i]]
	# 	res[i] = min(cnt)-i if cnt else 0

	# return res

