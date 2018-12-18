def trailingZeroes(n):
	# computed = {1:1}
	# def calc_inner(n):
	# 	if n not in computed:
	# 		computed[n] = trailingZeroes(n-1) * n
	# 	return computed[n]
	# return calc_inner(n)

	## time exceed
	# if n < 3: return 0
	# a, b = 1, 2
	# for i in range(3, n+1):
	# 	a, b = b, b*i
	# # return b
	# return len(str(b)) - len(str(int((str(b)[::-1]))))
	ans = 0
	while n >0:
		ans += n // 5
		n //= 5
	return ans
print(trailingZeroes(2))