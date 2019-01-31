def consecutiveNumbersSum(N):
	## 等差数列 方差为1
	## (x + (x+(m-1))) * m // 2 = N
	## mx + m * (m-1) // 2 = N
	m = 1
	ans = 0
	while m <= N:
		mx = N - m * (m-1) // 2
		print(mx, m )
		if mx <= 0:
			break
		if mx % m == 0:
			ans += 1

		m += 1

	return ans 

print(consecutiveNumbersSum(15))