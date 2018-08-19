def countPrimes(n):
	## can't AC
	# result = []
	# if n == 2:
	# 	return 0
	# elif n > 2:
	# 	for ele in range(2, n):
	# 		for i in range(2, ele):
	# 			if ele % i == 0:
	# 				break
	# 		else:
	# 			result.append(ele)

	# return len(result)
	if n < 3:
		return 0

	digits = [1 if ele > 1 else 0 for ele in range(n)]
	print(digits)
	for i in range(2, int(n**0.5)+1):
		if digits[i]== 1:
			for j in range(i+i, n, i):
				digits[j] = 0
	return sum(digits)



n = 10
print(countPrimes(n))
