def findNthDigit(n):
	## can't ac
	# return int("".join(str(char) for char in list(range(1, n+1)))[n-1])

	## way1
	if n <= 9: return n
	i, p = 1, 9
	while True:
		n += p 
		p = p * 10 + 9
		i += 1
		if n < p * i:
			return int(str(int((n+i-1)//i))[(n+i-1)%i])
	# start, size, step = 1,1,9
	# while n > size * step:
	# 	n, size, step, start = n-(size*step), size + 1, step*10, start * 10

	# return int(str(start+(n-1)))
	

print(findNthDigit(3))