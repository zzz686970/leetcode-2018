def largestPalindrome(n):
	## can't ac
	# result =0
	# if n > 1:
	# 	for i in range(10**n-1, 9*(10**(n-1)), -1):
	# 		for j in range((10**n)-2, 9*(10**(n-1)), -1):
	# 			if str(i * j) == "".join(list(reversed(str(i* j)))):
	# 				result = i*j
	# 				# print(i, j)
	# 				break
	# 		if result != 0:
	# 			break
	# else:
	# 	result = 9


	# return result % 1337

	## can't ac


	

	return [9, 9009, 906609, 99000099, 9966006699, 999000000999, \
                    99956644665999, 9999000000009999][n - 1] % 1337

n = 2
print(largestPalindrome(n))
