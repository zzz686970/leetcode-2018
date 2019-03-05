## binary search
def isPefectSquare(num):
	if num < 1: return False 
	## in case of small number like 1, 4, so r = num
	l, r= 0, num 
	while l < r:
		mid = (l + r) // 2
		if mid **  2 < num:
			l = mid + 1
		else:
			r = mid 
	return l ** 2 == num 

def isPerfectSquare(num):
	p = num
	while p ** 2 > num:
		p = (p+num//p) //2

	return p * p == num 

assert True == isPerfectSquare(16)


def isPerfectSquare(num):
	if num == 1: return True 
	l, r = 0, num
	while l <= r:
		mid = (l + r) // 2
		if mid ** 2 == num:
			return True 
		elif mid ** 2 < num:
			l = mid + 1
		else:
			r = mid - 1
	print(l, r)
	return False

print(isPerfectSquare(18))
# assert True == isPerfectSquare(16)