def countNumbersWithUniqueDigits(n):
	## after picking one number, the options for the following digit would decrease by 1
	## one-digit number range from 1-9, while 2-digit number can have 0
	options = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
	ans, product = 1, 1
	for i in range(min(n, 10)):
		product *= options[i]
		ans += product 

	return ans 

