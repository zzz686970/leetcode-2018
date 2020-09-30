def count_ways(n):
	"""how many ways to reach the stairs
	
	can be 1, 2, 3 steps each time
	
	Arguments:
		n {int} -- number of stairs
	"""
	a, b, c = 1, 2, 4
	if n == 1: return a 
	if n == 2: return b 
	for i in range(3, n):
		a, b, c = b, c, a+b+c 

	return c 

if __name__ == '__main__':
	print(count_ways(1))
	print(count_ways(2))
	print(count_ways(3))
	print(count_ways(4))
	print(count_ways(5))
	print(count_ways(100))