def reorderedPowerOf2( N):
	"""
	:type N: int
	:rtype: bool
	"""
	import collections 
	## way 1
	# table = dict()
	# for i in range(0, 31):
	# 	if 2 ** i > 10 ** 9:
	# 		break
	# 	else:
	# 		if len(str(2**i)) not in table:
	# 			table[len(str(2**i))] =  [2 ** i]
	# 		else:
	# 			table[len(str(2**i))] +=  2 ** i,
	# print(table)

	# for x in table[len(str(N))]:
	# 	if Counter(list(str(x))) == Counter(list(str(N))):
	# 		return True


	# return False 
	test = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]

	table = list(map(lambda x: (len(str(x)),x),test))
	# table = list(map(lambda n: 1 << n , range(100)))
	print(*table)

	## concise version
	cnt = collections.Counter(str(N))
	for x in range(32):
		if cnt == collections.Counter(str(1<<x)):
			return True 

	return False

print(reorderedPowerOf2(10))