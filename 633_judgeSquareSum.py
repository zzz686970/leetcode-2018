import math
def judgeSquareSum(c):
	if c == 0:
		return True
	for i in range(1, int(math.sqrt(c)+1)):
		b = math.sqrt(c- i ** 2)
		if b == int(b):
			return True
	return False

print(judgeSquareSum(25))