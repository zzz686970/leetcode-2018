def isUgly(num):
	if num <=0: return False
	for x in (5,3,2):
		while num % x == 0:
			num //= x 
	return num == 1

assert True == isUgly(6)
assert True == isUgly(8)
assert False == isUgly(14)