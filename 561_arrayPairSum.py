def arrayPariSum(nums):
	b = sorted(nums)
	result = 0
	for n in range(len(b)):
		if n % 2 == 0:
			result += b[n]

	return result

a = [1,4,3,2]
print(arrayPariSum(a))