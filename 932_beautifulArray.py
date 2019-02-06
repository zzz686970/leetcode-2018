def beautifulArray(N):
	def recursive(arr):
		if len(arr) < 2: return arr 
		return recursive(arr[::2]) + recursive(arr[1::2])

	return recursive(list(range(1, N+1)))

print(beautifulArray(4))