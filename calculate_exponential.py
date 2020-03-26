def exponential(n, x):
	res = 1.0
	for i in range(n, 0, -1):
		res = 1 + x * res / i

	return f"e^{x} = {res}"

print(exponential(17, 3))