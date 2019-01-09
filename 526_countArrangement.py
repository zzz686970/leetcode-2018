def countArrangement(N):
	def count(i, sets):
		if i == 1: return 1
		return sum(count(i-1, sets-{x}) for x in sets if x % i ==0 or i % x == 0)

	return count(N, set(range(1,N+1)))


print(countArrangement(2))