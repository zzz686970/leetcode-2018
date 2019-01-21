def divide(dividend, divisor):
	if (dividend == -2 ** 31 and divisor == -1): return 2 ** 31 -1
	sign = 1 if (dividend >0) == (divisor>0) else -1
	dividend, divisor = abs(dividend), abs(divisor)
	res = 0
	while dividend >= divisor:
		tmp, i = divisor, 1
		while dividend >= tmp:
			print(dividend, res, i, tmp)
			dividend -= tmp 
			res += i 
			tmp <<= 1
			i <<= 1
			

	return res * sign

print(divide(1, 1))

