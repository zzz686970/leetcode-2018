def findNthDigit(n):
	## can't ac
	# return int("".join(str(char) for char in list(range(1, n+1)))[n-1])

	## way1
	# if n <= 9: return n
	# i, p = 1, 9
	# while True:
	# 	n += p 
	# 	p = p * 10 + 9
	# 	i += 1
	# 	if n < p * i:
	# 		return int(str(int((n+i-1)//i))[(n+i-1)%i])

	# start, size, step = 1,1,9
	# while n > size * step:
	# 	n, size, step, start = n-(size*step), size + 1, step*10, start * 10

	# return int(str(start+(n-1)))

	## way2 
	# 1000 -> 9 + 180 + 811
	# 811 is 810th, 810 // 3 = 270, 810 % 3 = 0
	bits = [9 * (10 **i) *(i+1) for i in range(10)] ## 1-9 9; 10-99 90 * 2; 100-999 900 * 3
	num_section = [(10**i, 10**(i+1) -1) for i in range(10)]
	for i in range(len(num_section)):
		if n - bits[i] <=0:
			return int(str(num_section[i][0] + (n-1)//(i+1))[(n-1)%(i+1)])
			## base 100		+	270  [0]
		else:
			n -= bits[i]
	print(num_section)
	

print(findNthDigit(11))