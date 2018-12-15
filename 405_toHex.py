def toHex(num):
	ans = ''
	d = {k:v for k,v in zip(range(10,17), 'abcdef')}
	print(d)
	if num == 0: return '0'
	if num < 0: num+= 4294967296
	
	while num > 0:
		temp = num % 16
		if temp >=10:
			ans = d[temp] + ans
		else:
			ans = str(temp) + ans 
		num //= 16

	return ans


print(toHex(26))