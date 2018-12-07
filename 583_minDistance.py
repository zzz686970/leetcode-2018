def minDistance(word1, word2):
	## Wring solution
	# if not word1: return len(word2)
	# if not word2: return len(word1)

	# pre = [j for j in range(len(word2) + 1)]

	# for i in range(len(word1)):
	# 	cur = [i + 1]
	# 	for j in range(len(word2)):
	# 		if word2[j] == word1[i]:
	# 			cur.append(pre[j])
	if not word1 and not word2 : return 0
	if not word1: return len(word2)
	if not word2: return len(word1)

	m, n = len(word1), len(word2)
	# dp = [[0] * (n+1) for i in range(m+1)]
	dp = [[0 for _ in range(m+1)] for _ in range(n)]
	for i in range(n):
		for j in range(m):
			if word2[i] == word1[j]:
				dp[i][j] = dp[i-1][j-1] + 1
			else:
				dp[i][j] = max(dp[i-1][j-1], dp[i][j-1])
	
	return m+n - (2 * max(dp[-1]))

print(minDistance('b',''))
