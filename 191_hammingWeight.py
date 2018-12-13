def hammingWeight(n):
	return sum(int(el) for el in bin(abs(n))[2:])
	## way 2
	# return bin(n)[2:].count('1')

	## way 3
	# cnt = 0
	# while n:
	# 	n &= n-1
	# 	cnt += 1
	# return cnt


print(hammingWeight(128))