def isHappy(n):

	pool = set()
	while n not in pool:
		pool.add(n)
		n = sum([int(c)**2 for c in str(n)])

	print(pool)
	return n == 1

print(isHappy(100))