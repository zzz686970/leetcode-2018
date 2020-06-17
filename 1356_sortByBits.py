def sortByBits(arr):
	return sorted(arr, key = lambda a: [bin(a).count('1'), a])
	return sorted(arr, key = lambda x: (sum((x >> i) & 1 for i in range(32)), x))