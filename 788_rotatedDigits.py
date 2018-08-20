def rotatedDigits(N):
	ans = 0
	result = []
	for num in range(N+1):
		if all(char in ['0','1','2','5','6','8','9'] for char in str(num)) and any(char in ['2','5','6', '9'] for char in str(num)):
			ans += 1


	return ans

print(rotatedDigits(857))