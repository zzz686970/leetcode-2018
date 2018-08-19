def countPrimeSetBits(L, R):
	result = dict()
	ans = set()
	test = dict()
	for ele in range(L, R+1):
		result[ele] = bin(ele).count('1')
	for key, value in result.items():
		if value == 2:
			ans.add(key)
		elif value > 2:
			for i in range(2, value):
				if value % i == 0:
					break
			else:
				ans.add(key)
	# for key, value in result.items():
	# 	if key in ans:
	# 		test[key] = value
	return len(ans)


L = 990
R = 1048
print(countPrimeSetBits(L, R))