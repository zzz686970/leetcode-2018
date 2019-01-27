def nthUglyNumber(n):
	# res = [1]
	# p1, p2, p3 = 0, 0, 0
	# while n > 1:
	# 	v1, v2, v3 = 2 * res[p1], 3 * res[p2], 5 * res[p3]
	# 	next_ele = min(v1, v2, v3)
	# 	if next_ele == v1:
	# 		p1 += 1
	# 	if next_ele == v2:
	# 		p2 += 1
	# 	if next_ele == v3:
	# 		p3 += 1

	# 	res.append(next_ele)
	# 	n -= 1

	# return res[-1]
	
	res = [1]
	p1, p2, p3 = 0, 0, 0
	while n > 1:
		v1, v2, v3 = 2 * res[p1], 3 * res[p2], 5 * res[p3]
		next_ele = min(v1, v2, v3)
		if next_ele == v1:
			p1 += 1
		if next_ele == v2:
			p2 += 1
		if next_ele == v3:
			p3 += 1
		res.append(next_ele)
		n -= 1
	return res[-1]

	## optimize
	# class Solution():
		# ugly = sorted(2**a * 3**b * 5**c
		# 			  for a in range(32) for b in range(20) for c in range(14))
		# def nthUglyNumber(self, n):
		# 	return self.ugly[n-1]

# for i in range(10):
print(nthUglyNumber(10))