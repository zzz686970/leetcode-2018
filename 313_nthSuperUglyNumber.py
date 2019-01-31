def nthSuperUglyNumber(n, primes):
	import heapq
	prime_list = [(primes[i],primes[i], 0) for i in range(len(primes))]
	res = [1]

	while len(res) < n:
		val, prm, idx = heapq.heappop(prime_list)

		if val <= res[-1]:
			while val <= res[-1]:
				idx += 1
				val = prm * res[idx]
		else:
			res += val,
			idx += 1
			val = prm * res[idx]
			# val, idx = prm * res[idx+1], idx + 1

		heapq.heappush(prime_list, (val, prm, idx))


	return res[-1]