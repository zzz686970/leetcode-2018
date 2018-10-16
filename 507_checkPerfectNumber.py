def checkPerfectNumber(num):
	if num < 0:
		return False
	ans = 0
	mid = int(num** 0.5)
	ans = sum(i + num//i for i in range(1, mid+1) if not num% i)
	print(ans)
	if num == mid ** 2: ans -= mid
	return num == ans - num

print(checkPerfectNumber(28))