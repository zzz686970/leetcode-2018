def minimumDeleteSum(s1, s2):
	# dp = [
	l1, l2 = len(s1), len(s2)

	dp = [[0]* (l2+1) for _ in range(l1+1)]
	for i in range(l1):
		for j in range(l2):
			if s1[i] == s2[j]:
				dp[i+1][j+1] = dp[i][j] + ord(s1[i])
			else:
				dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

	result = sum(map(ord, s1+s2)) - dp[-1][-1] * 2

	return result

print(minimumDeleteSum(s1 = "sea", s2 = "eat"))