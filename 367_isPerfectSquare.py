def isPerfectSquare(num):
	p = num
	while p ** 2 > num:
		p = (p+num//p) //2

	return p * p == num 

assert True == isPerfectSquare(16)