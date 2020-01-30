## 一只兔子 ，在第 5 到 10 天每天生一只，第 10 天后死亡，开始有 1 只兔子，问第 100 天有几只兔子
dp = [1] +[0] * 99

for i in range(100):
	if 4 <= i < 10:
		for j in range(i-3):
			dp[i] += dp[j]
	elif i >= 10 :
		for j in range(i-9, i-3):
			dp[i] += dp[j]
	if i <= 9:
		print(f'day {i+1} total: {sum(dp[:i+1])}')
	else:
		print(f'day {i+1} total: {sum(dp[i-9:i+1])}')


