def numberOfSteps(n):
	step, res = 0, n
	while res > 0:
		res = res - 1 if res % 2 else res // 2
		step += 1
	return step

def numberOfSteps_2(n):
	digits = f'{n:b}'
	print(digits)
	return digits.count('1') - 1 + len(digits)

if __name__ == '__main__':
	print(numberOfSteps_2(8))